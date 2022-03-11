from django.contrib import admin

from .models import Post, Group  # импортируем модели из models.py


# модель PostAdmin регистрирует представление
# моделей Post и Group в базе данных
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk',  # Перечисляем поля, которые
                    'text',  # должны отображаться в админке
                    'pub_date',
                    'author',
                    'group',)

    list_editable = ('group',)  # Возможность ред-ть группы в БД
    search_fields = ('text',)  # Интерфейс для поиска по тексту постов
    list_filter = ('pub_date',)  # Добавляем возможность фильтрации по дате

    empty_value_display = '-пусто-'  # в пустой колонке будет эта строка


# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Post, PostAdmin)
admin.site.register(Group)