from django.urls import reverse
import pytest
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_get_course(course_factory, api_client):
    course = course_factory()
    url = reverse('courses-detail', args=[course.id])
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    ids = resp_json['ids']
    assert len(ids) == 1


@pytest.mark.django_db
def test_course_list(course_factory, api_client):
    courses = course_factory(_quantity=4)
    url = reverse('courses-list')
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert len(courses) == len(resp_json)


@pytest.mark.django_db
def test_filter_id(course_factory, api_client):
    url = reverse('courses-list')
    courses = course_factory(_quantity=4)
    id = courses[0].id
    resp = api_client.get(url, {"id": id})
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json[0]['id'] == id


@pytest.mark.django_db
def test_filter_name(api_client, course_factory):
    url = reverse('courses-list')
    course = course_factory(name='Python')
    params = {
        'name': 'Python'
    }
    resp = api_client.get(url, params)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json['name'] == course.name


@pytest.mark.django_db
def test_create_course(api_client):
    url = reverse('courses-list')
    params = {
        'name': 'Математика'
    }
    resp = api_client.post(url, params)
    assert resp.status_code == HTTP_201_CREATED
    resp_json = resp.json()
    assert resp_json['name'] == params['name']



@pytest.mark.django_db
def test_update_course(course_factory, student_factory, api_client):
    course = course_factory()
    new_course = course_factory()
    url = reverse('courses-detail', args=[course.id])
    params = {
        'id': new_course.id
    }
    resp = api_client.create(url, params)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json['name'][0] == new_course.id

@pytest.mark.django_db
def test_success_delete(course_factory, api_client):
    course = course_factory()
    url = reverse('courses-detail', args=[course.id])
    resp = api_client.delete(url)
    assert resp.status_code == HTTP_204_NO_CONTENT

