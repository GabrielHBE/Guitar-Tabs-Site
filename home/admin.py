from django.contrib import admin

from home import models

# Register your models here.
@admin.register(models.Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('id','song_name','song_author','show')
    ordering = ('id',)
    search_fields = ('id','song_name','song_author',)
    list_per_page = 10
    #list_editable = ('first_name','last_name','show')
    list_display_links = ('id','song_name',)


@admin.register(models.Style)
class StyleAdmin(admin.ModelAdmin):
    #list_display = ('song_name',)
    ordering = ('-id',)

@admin.register(models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    #list_display = ('song_name',)
    ordering = ('-id',)

@admin.register(models.Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    #list_display = ('song_name',)
    ordering = ('-id',)