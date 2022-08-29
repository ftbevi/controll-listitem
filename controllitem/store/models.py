from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="Criado às", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Atualizado às", auto_now=True)
    deleted_at = models.DateTimeField(
        verbose_name="Deletado às", blank=True, null=True, default=None
    )


class ListItem(BaseModel):
    user = models.ForeignKey(
        User, verbose_name="owner", on_delete=models.PROTECT
    )
    description = models.CharField(
        verbose_name='description', max_length=255, blank=True)

    class Meta:
        verbose_name = 'List Item'
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.description}"


class Item(BaseModel):
    user = models.ForeignKey(
        User, verbose_name="owner", on_delete=models.PROTECT
    )
    list_item = models.ForeignKey(
        ListItem, verbose_name="origin list", related_name="itens", on_delete=models.PROTECT
    )
    child_item = models.ForeignKey(
        "Item", verbose_name="child item", null=True, blank=True, on_delete=models.PROTECT
    )
    description = models.CharField(verbose_name='description', max_length=255, blank=True)
    quantity = models.IntegerField(verbose_name='quantity', null=True, blank=True)

    class Meta:
        verbose_name = 'Item'
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.description}"

    def save(self, *args, **kwargs):
        if self.user.email == self.list_item.user.email:
            raise ValidationError(f"{self.user.email} user list and user list are equals.")
        super().save(*args, **kwargs)
