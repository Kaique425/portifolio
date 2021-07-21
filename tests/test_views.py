import pytest
from paginas.models import Projeto
from django.urls import resolve, reverse
from  pytest_django.asserts import assertTemplateUsed


pytestmark = pytest.mark.django_db


@pytest.fixture
def home_response(client):
    return client.get(reverse('paginas:home'))

@pytest.fixture
def project_response(client):
    proj1 = Projeto.objects.create(nome="To do list",descricao="Uma lista de tarefas",projlink="www.todolist.com",slug="To-do-list")
    return client.get(reverse('paginas:projeto', kwargs={"slug":proj1.slug}))
    

class TestHomePageView:
    
    
    def test_reverse_resolve(self):
        assert reverse("paginas:home") == "/"
        assert resolve("/").view_name == "paginas:home"

    def test_home_status_code(self, home_response):
        assert home_response.status_code == 200
    
    def test_template(self, home_response):
        assertTemplateUsed(home_response, "paginas/home.html")

class TestProjectPageView:

    
    def test_reverse_resolve(self):
        url = reverse("paginas:projeto", kwargs={"slug": "Test-slug"})
        assert url == f'/projeto/Test-slug'
        
        view_name = resolve('/projeto/Test-slug').view_name
        assert  view_name == "paginas:projeto"
    
    def test_status_code(self, project_response):
        assert project_response.status_code == 200