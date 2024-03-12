# from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.django_udemy.companies.models import Company
from api.django_udemy.companies.serializers import CompanySerializer
from fibonacci.dynamic import fibonaci_dynamic_v2


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination


# @api_view(http_method_names=["POST"])
# def send_company_email(request: Request) -> Response:
#     """
#     sends email with request payload
#     sender: israeltechlayoffs@gmail.com
#     receiver: israeltechlayoffs@gmail.com
#     """
#     send_mail(
#         subject=request.data.get("subject"),
#         message=request.data.get("message"),
#         from_email="israeltechlayoffs@gmail.com",
#         recipient_list=["israeltechlayoffs@gmail.com"],
#     )
#     return Response(
#         {"status": "success", "info": "email sent successfully"}, status=200
#     )


@api_view(http_method_names=["GET"])
def fibonacci_view(request: Request) -> Response:
    bad_response = Response(
        data={"error": "query number must be a positive integer or 0"},
        status=400,
    )
    num: str = request.query_params.get("n")
    if num is not None:
        try:
            num_int = int(num)
            if num_int >= 0:
                return Response(
                    data={"fibonacci": fibonaci_dynamic_v2(num_int)},
                    status=200,
                )
            else:
                return bad_response
        except ValueError:
            return bad_response
    else:
        return bad_response
