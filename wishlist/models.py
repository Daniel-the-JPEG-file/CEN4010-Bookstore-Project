from django.db import models


class WishlistItem(models.Model):
    book_title = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255, blank=True)
    book_id = models.IntegerField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    wishlist_name = models.CharField(max_length=100, default="Primary Wishlist")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_title