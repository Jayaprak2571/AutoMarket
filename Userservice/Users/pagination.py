from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
class CustomPagination(PageNumberPagination):
    page_size=3
    page_size_query_param = 'page_size'
    max_page_size=5
    def get_paginated_response(self,data):
        return Response({
            'page':self.page.number,
            'page_size':self.page.paginator.per_page,
            'total_items':self.page.paginator.count,
            'total_pages':self.page.paginator.num_pages,
            'next':self.get_next_link(),
            'previous':self.get_previous_link(),
            'results':data
        })

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 100
    def get_paginated_response(self, data):
        return Response({
            'limit': self.limit,
            'offset': self.offset,
            'total_items': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })