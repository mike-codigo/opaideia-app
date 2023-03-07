from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'user_image']

class InstructorsAdmin(admin.ModelAdmin):
    fields = ['user', 'courses']
    list_display = ['user', 'get_courses']

    def get_courses(self, obj):
        return "\n".join([c.title for c in obj.courses.all()])

class StudentsAdmin(admin.ModelAdmin):
    fields = ['user', 'courses']
    list_display = ['user', 'get_courses']

    def get_courses(self, obj):
        return "\n".join([c.title for c in obj.courses.all()])

class DocsAdmin(admin.ModelAdmin):
    fields = ['file', 'type', 'area', 'topic']
    list_display = ['id', 'file', 'type', 'get_area', 'get_topic']

    def get_area(self, obj):
        return "\n".join([a.name for a in obj.area.all()])
    def get_topic(self, obj):
        return "\n".join([t.name for t in obj.topic.all()])

class SciencesAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']

class SubAreaAdmin(admin.ModelAdmin):
    fields = ['name', 'science']
    list_display = ['name', 'sciences']

    def sciences(self, obj):
        return "\n".join([s.name for s in obj.science.all()])

class SubTopicAdmin(admin.ModelAdmin):
    fields = ['name','sub_area']
    list_display = ['name', 'sub_areas']

    def sub_areas(self, obj):
        return "\n".join([a.name for a in obj.sub_area.all()])

class StudysAdmin(admin.ModelAdmin):
    fields = ['title', 'public','user_create', 'credit', 'area', 'topic', 'content', 'summary', 'pdf', 'teaching_audio', 'rev1_date', 'rev2_date', 'rev3_date', 'rev4_date']
    list_display = ['title', 'public','user_create', 'credit', 'areas', 'topics']

    def areas(self, obj):
        return "\n".join([a.name for a in obj.area.all()])
    def topics(self, obj):
        return "\n".join([t.name for t in obj.topic.all()])

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'user_create', 'description', 'start_time', 'end_time']

class CoursesAdmin(admin.ModelAdmin):
    fields = ['title', 'lessons', 'cover_image', 'topics', 'areas', 'rooms', 'hard_skills', 'course_model', 'duration', 'certificate', 'instructors', 'credits']
    list_display = ['title', 'course_model', 'duration', 'get_lessons']

    def get_lessons(self, obj):
        return "\n".join([l.title for l in obj.lessons.all()])

class RoomsAdmin(admin.ModelAdmin):
    fields = ['course', 'max_students', 'students', 'course_days', 'course_schedule', 'duration']
    list_display = ['course', 'course_days', 'course_schedule', 'duration', 'max_students', 'get_students']

    def get_students(self, obj):
        return "\n".join([s.students for s in obj.students.all()])

class LessonsAdmin(admin.ModelAdmin):
    fields = ['title', 'course', 'video', 'audio', 'notes', 'slides', 'source_code', 'subtitles', 'transcript', 'hard_skills', 'projects']
    list_display = ['title', 'course', 'video', 'get_hard_skills', 'get_projects']

    def get_hard_skills(self, obj):
        return "\n".join([h.name for h in obj.hard_skills.all()])

    def get_projects(self, obj):
        return "\n".join([h.title for h in obj.projects.all()])

class ProjectsAdmin(admin.ModelAdmin):
    fields = ['lessons', 'title', 'cover_image', 'delivery_date', 'start_file', 'getting_started', 'description', 'hints', 'specifications', 'how_to_send']
    list_display = ['title', 'lessons', 'delivery_date', 'start_file']

class HardSkillsAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']

class SoftSkillsAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']

class CertificatesAdmin(admin.ModelAdmin):
    fields = ['name', 'institutions', 'course', 'icon', 'nivel']
    list_display = ['name', 'get_institutions', 'course', 'icon', 'nivel']

    def get_institutions(self, obj):
        return "\n".join([i.institutions for i in obj.institutions.all()])

class InstitutionsAdmin(admin.ModelAdmin):
    fields = ['name', 'logo', 'courses']
    list_display = ['name', 'logo', 'get_courses']

    def get_courses(self, obj):
        return "\n".join([h.name for h in obj.courses.all()])



admin.site.register(User, UserAdmin)
admin.site.register(Instructors, InstructorsAdmin)
admin.site.register(Students, StudentsAdmin)
admin.site.register(Docs, DocsAdmin)
admin.site.register(Sciences, SciencesAdmin)
admin.site.register(SubArea, SubAreaAdmin)
admin.site.register(SubTopic, SubTopicAdmin)
admin.site.register(Studys, StudysAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Rooms, RoomsAdmin)
admin.site.register(Lessons, LessonsAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(HardSkills, HardSkillsAdmin)
admin.site.register(SoftSkills, SoftSkillsAdmin)
admin.site.register(Certificates, CertificatesAdmin)
admin.site.register(Institutions, InstitutionsAdmin)