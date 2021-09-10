from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class CustomPageNumberPagination(PageNumberPagination):
    # Elements to show on a single page
    page_size = 5
    # Custom parameter name
    page_query_param = 'p'
    # Amounts of elements user wants to display on a single page
    page_size_query_param = 'records'
    # Maximum element size on a single page
    max_page_size = 10
    # Custom last page query parameter
    last_page_strings = 'end'


class CustomLimitOffsetPagination(LimitOffsetPagination):
    # Elements to show on a single page
    default_limit = 5
    # Custom limit parameter name
    limit_query_param = 'perpage'
    # Custom offset parameter name
    offset_query_param = 'starting'
    # Maximum element size on a single page
    max_limit = 5
