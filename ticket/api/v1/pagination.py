from rest_framework import pagination

class ScanLogsPagination(pagination.PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 10
    page_query_param = 'p'
    

class TicketPagination(pagination.PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 10
    page_query_param = 'p'