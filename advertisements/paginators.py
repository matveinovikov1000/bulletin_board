from rest_framework.pagination import PageNumberPagination


class CustomPaginator(PageNumberPagination):
    page_size = 4
    page_size_query_param = 4
    max_page_size = 10
