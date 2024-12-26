import io
import json
from typing import List

from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseServerError
from django_reportbroD.models import ReportDefinition
from reportbro import Report, ReportBroError

from ..models import *


def custom_export_report_by_name(template_name, data, file="reporte", send_email=False):
    """Export a report using its name"""

    report = ReportDefinition.objects.filter(name=template_name).first()

    if not report:
        return HttpResponseServerError("Este reporte no se encuentra disponible")

    return customReportPDF(
        report.report_definition,
        data,
        file,
    )


def customReportPDF(
    report_definition,
    data,
    file="reporte",
):
    try:
        report_inst = Report(json.loads(report_definition), data)

        if report_inst.errors:
            raise ReportBroError(report_inst.errors[0])

        pdf_report = report_inst.generate_pdf()

        response = HttpResponse(bytes(pdf_report), content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="{filename}"'.format(
            filename=f"{file}.pdf"
        )

        return response
    except Exception as e:
        # Handle any exceptions or errors that may occur during the process
        print(f"An error occurred: {str(e)}")
        return HttpResponse("An error occurred while processing the report")


def generar_reporte_expediente_lectura_pdf(modeladmin, request, queryset):
    entidades: List[Lecturade_libro] = queryset
    lista = []
    for entidad in entidades:
        lista.append(
            {
                "suscriptor": str(entidad.suscriptor.nombre),
                "libro": str(entidad.libro.titulo),
                "fecha": entidad.fecha,
            }
        )

    data = {"lista": lista}

    return custom_export_report_by_name(
        "Expediente de Lectura", data, file="reporte", send_email=True
    )


def generar_reporte_prestamo_pdf(modeladmin, request, queryset):
    entidades: List[Prestamo] = queryset
    lista = []
    for entidad in entidades:
        lista.append(
            {
                "suscriptor": str(entidad.suscriptor.nombre),
                "libro": str(entidad.libro.titulo),
                "fecha": entidad.fecha_prestamo,
                "fecha_entrega": entidad.fecha_entrga,
            }
        )

    data = {"lista": lista}

    return custom_export_report_by_name(
        "Prestamos", data, file="reporte", send_email=True
    )


def generar_reporte_informe_asistencia_pdf(modeladmin, request, queryset):
    entidades: List[Asistencia] = queryset
    lista = []
    for entidad in entidades:
        lista.append(
            {
                "trabajador": str(entidad.trabajador.nombre),
                "expediente": str(entidad.trabajador.expediente),
                "fecha": entidad.fecha,
                "horas": str(entidad.horas),
            }
        )

    data = {"lista": lista}

    return custom_export_report_by_name(
        "Informe de asistencia", data, file="reporte", send_email=True
    )
