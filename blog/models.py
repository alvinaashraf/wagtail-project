from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.snippets.models import register_snippet
from modelcluster.models import ParentalKey
from taggit.models import TaggedItemBase
from modelcluster.tags import ClusterTaggableManager

# Create your models here.


class BlogPage(Page):
    description = models.CharField(max_length=100, blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]


class PostPage(Page):
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.CASCADE,
        related_name="blog_image",
        null=True,
    )
    description = models.CharField(max_length=100, blank=True, null=True)
    tags = ClusterTaggableManager(through="PostPagetag", blank=True)
    blog_category = models.ForeignKey(
        "BlogCategory", blank=True, on_delete=models.CASCADE, related_name="post_pages"
    )
    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("tags"),
        FieldPanel("blog_category"),
        FieldPanel("description"),
    ]


class PostPageBlogCategory(models.Model):
    page = ParentalKey(
        "blog.PostPage",
        on_delete=models.CASCADE,
        blank=True,
        related_name="categories",
    )

    content_panels = Page.content_panels + [
        FieldPanel("page"),
    ]


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(max_length=80, unique=True)
    content_panels = Page.content_panels + [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    def __str__(self):
        return self.name


class PostPagetag(TaggedItemBase):
    content_object = ParentalKey("blog.PostPage", blank=True)
