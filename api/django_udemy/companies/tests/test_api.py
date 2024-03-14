import json

import pytest
from django.urls import reverse

from api.django_udemy.companies.models import Company

companies_url = reverse("companies-list")
pytestmark = pytest.mark.django_db


# ------------------- Test GET Companies -------------------


def test_zero_companies_should_return_empty_list(client):
    response = client.get(companies_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


@pytest.fixture
def amazon() -> Company:
    return Company.objects.create(name="Amazon")


def test_one_company_exists_succeed(client, amazon):
    response = client.get(companies_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("name") == amazon.name
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""

    amazon.delete()


@pytest.fixture()
def company(**kwargs):
    def _company_factory(**kwargs) -> Company:
        company_name = kwargs.pop("name", "Test Company INC")
        return Company.objects.create(name=company_name, **kwargs)

    return _company_factory


def test_multiple_companies_exist_ok(client, company):
    tiktok: Company = company(name="Tiktok")
    twitch: Company = company(name="Twitch")
    test_company: Company = company()
    company_names = {tiktok.name, twitch.name, test_company.name}
    response_companies = client.get(companies_url).json()
    assert len(company_names) == len(response_companies)
    response_company_names = set(
        map(lambda company: company.get("name"), response_companies)
    )
    assert company_names == response_company_names


# ------------------- Test POST Companies -------------------


def test_create_company_without_arguments_fail(client):
    response = client.post(path=companies_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {"name": ["This field is required."]}


def test_create_existing_company_fail(client):
    Company.objects.create(name="apple")
    response = client.post(
        path=companies_url,
        data={"name": "apple"},
    )
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "name": ["company with this name already exists."]
    }


def test_create_company_with_only_name_other_fields_default(client):
    response = client.post(
        path=companies_url,
        data={"name": "test_company_name"},
    )
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("name") == "test_company_name"
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""


def test_create_company_with_layoffs_success(client):
    response = client.post(
        path=companies_url,
        data={"name": "test_company_name", "status": "Layoffs"},
    )
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("status") == "Layoffs"


def test_create_company_with_wrong_status_fail(client):
    response = client.post(
        path=companies_url,
        data={"name": "test_company_name", "status": "wrong_status"},
    )
    assert response.status_code == 400
    assert "wrong_status" in str(response.content)
    assert "is not a valid choice" in str(response.content)
