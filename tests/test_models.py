from django.test.testcases import TestCase
from paginas.models import Projeto

class ModelTestCase(TestCase):
    
    
    def setUp(self):
        proj1 = Projeto.objects.create(
            nome="To do list",
            descricao="Uma lista de tarefas",
            projlink="www.todolist.com",
            slug="To-do-list"
            )

    def test_if_project_name_is_equal_nome(self):
        proj1 = Projeto.objects.get(id=1)
        self.assertEqual(proj1.nome, "To do list")

    def test_the_project_link(self):
        proj1 = Projeto.objects.get(id=1)
        self.assertEqual(proj1.projlink, "www.todolist.com")

    def test_project_description(self):
        proj1 = Projeto.objects.get(id=1)
        self.assertEqual(proj1.descricao, "Uma lista de tarefas")

    def test_project_slug(self):
        proj1 = Projeto.objects.get(id=1)
        self.assertEqual(proj1.slug, "to-do-list")