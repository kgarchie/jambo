from rest_framework.pagination import PageNumberPagination


class UsersPagination(PageNumberPagination):
    page_size = 50
    page_query_param = 'page'
    max_page_size = 100
