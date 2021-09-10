from rest_framework.throttling import UserRateThrottle


class AdminRateThrottle(UserRateThrottle):
    scope = 'admin'


class EmployeeRateThrottle(UserRateThrottle):
    scope = 'employee'
