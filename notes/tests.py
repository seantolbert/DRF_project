from django.test import TestCase
from django.contrib.auth.models import User
from notes.models import Note, Category


class Test_Create_Note(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789'
        )
        test_post = Note.objects.create(
            category_id=1,
            title='Note title',
            excerpt='excerpt here',
            content="note content",
            slug='post-title',
            author_id=1,
            status='published'
        )

    def test_notes_content(self):
        note = Note.noteobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{note.author}'
        excerpt = f'{note.excerpt}'
        title = f'{note.title}'
        content = f'{note.content}'
        status = f'{note.status}'
        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(content, 'Post Content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(note), "Post Title")
        self.assertEqual(str(cat), "django")
