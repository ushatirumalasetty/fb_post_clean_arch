from abc import ABC
from abc import abstractmethod
from typing import List
from fb_post_v2.interactors.storages.dtos import ReactionMetricesDto
from fb_post_v2.interactors.storages.dtos import *



class PresenterInterface:
   
    @abstractmethod
    def get_create_post_response(self, post_id:int):
        pass
    
    @abstractmethod
    def raise_exception_for_invalid_post(self):
        pass
    
    @abstractmethod
    def raise_exception_for_invalid_comment(self):
        pass

    @abstractmethod
    def get_create_comment_response(self, comment_id:int):
        pass

    @abstractmethod
    def get_reply_to_comment_response(self, reply_id:int):
        pass

    @abstractmethod
    def get_response_for_get_posts_with_more_positive_reaction(
            self,
            post_ids: List[int]):
        pass
    
    @abstractmethod
    def get_response_for_total_reaction_count(self, count: int):
        pass
    
    @abstractmethod
    def get_response_for_reaction_metrices(self, result:List[ReactionMetricesDto]):
        pass
    
    @abstractmethod
    def get_response_for_user_reacted_posts(self, post_ids: List[int]):
        pass
    
    @abstractmethod
    def get_response_for_get_post_response(self,
            post_reaction_dtos: PostReactionCompleteDetailsDto):
        pass
