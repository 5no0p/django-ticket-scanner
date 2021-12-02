from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response

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

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ("count", self.page.paginator.count),
                    ("next", self.get_next_link()),
                    ("previous", self.get_previous_link()),
                    ("total_pages", self.page.paginator.num_pages),
                    ("page", self.page.number),
                    ("results", data),
                ]
            )
        )