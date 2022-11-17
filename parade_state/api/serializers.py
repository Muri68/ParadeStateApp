from rest_framework.serializers import ModelSerializer
from parade_state.models import ParadeState

class ParadeStateSerializer(ModelSerializer):
    class Meta:
        model = ParadeState
        fields = [
            'id',
            'date',
            'author',
            'title',
            'posted_strength_officers',
            'posted_strength_soldiers',
           
        ]


# 'on_parade_officers',
# 'on_parade_soldiers',
# 'on_duty_officers',
# 'on_duty_soldiers',
# 'off_duty_officers',
# 'off_duty_soldiers',
# 'sick_report_officers',
# 'sick_report_soldiers',
# 'civil_institution_officers',
# 'civil_institution_soldiers',
# 'punishment_duty_officers',
# 'punishment_duty_soldiers',
# 'pass_officers',
# 'pass_soldiers',
# 'leave_officers',
# 'leave_soldiers',
# 'course_officers',
# 'course_soldiers',
# 'attached_officers',
# 'attached_soldiers',
# 'detached_officers',
# 'detached_soldiers',
# 'call_centre_officers',
# 'call_centre_soldiers',
# 'external_operations_officers',
# 'external_operations_soldiers',
# 'internal_operations_officers',
# 'internal_operations_soldiers',
# 'assignment_officers',
# 'assignment_soldiers',
# 'absent_officers',
# 'absent_soldiers',
# 'awol_officers',
# 'awol_soldiers',
# 'mess_officers',
# 'guard_room_soldiers',
# 'IHL_officers',
# 'IHL_soldiers',