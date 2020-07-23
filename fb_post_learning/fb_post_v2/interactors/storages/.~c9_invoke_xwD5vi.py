from abc import ABC
from abc import abstractmethod

from typing import Optional, List, Dict
from fb_post_v2.constants.enums import ReactionType
import datetime
from fb_post_v2.interactors.storages.dtos import Reacti


class StorageInterface(ABC):
    @abstractmethod
    def create_post(self, user_id:int, post_content:str)->int:
        pass

    @abstractmethod
    def create_comment(self, user_id:int, post_id:int, comment_content:str)->int:
        pass

    @abstractmethod
    def validate_post_id(self, post_id: int):
        pass

    @abstractmethod
    def validate_comment_id(self, comment_id: int):
        pass

    @abstractmethod
    def validate_reaction_type(self, reaction_type: str):
        pass


    @abstractmethod
    def react_to_post(self, user_id: int, post_id: int, reaction_type: str):
        pass

    @abstractmethod
    def validate_post_reaction_if_exists_get_reaction_type(
            self,
            user_id: int,
            post_id: int) -> Optional[ReactionType]:
        pass

    @abstractmethod
    def undo_post_reaction(self,
                           user_id: int,
                           post_id: int):
        pass

    @abstractmethod
    def update_post_reaction(self,
                             user_id: int,
                             post_id: int,
                             reaction_type: ReactionType):
        pass

    @abstractmethod
    def create_post_reaction(self,
                             post_id:int,
                             user_id:int,
                             reaction_type:ReactionType):
        pass

    @abstractmethod
    def react_to_comment(self, user_id: int, comment_id: int, reaction_type: str):
        pass

    @abstractmethod
    def validate_comment_reaction_if_exists_get_reaction_type(
            self,
            user_id: int,
            comment_id: int) -> Optional[ReactionType]:
        pass

    @abstractmethod
    def undo_comment_reaction(self,
                           user_id: int,
                           comment_id: int):
        pass

    @abstractmethod
    def update_comment_reaction(self,
                             user_id: int,
                             comment_id: int,
                             reaction_type: ReactionType):
        pass

    @abstractmethod
    def create_comment_reaction(self,
                             comment_id:int,
                             user_id:int,
                             reaction_type:ReactionType):
        pass

    @abstractmethod
    def reply_to_comment(self,
                         user_id: int,
                         comment_id: int,
                         reply_content: str):
        pass

    @abstractmethod
    def validate_comment_id_return_parent_comment_id(
            self,
            user_id: int,
            comment_id: int) ->int:
        pass

    @abstractmethod
    def get_posts_with_more_positive_reactions(self) -> List[int]:
        pass

    @abstractmethod
    def get_total_reaction_count(self)->int:
        pass


    @abstractmethod
    def get_reaction_metrices(self, post_id)->List[ReactionMetricesDto]:
        pass

    @abstractmethod
    def delete_post(self, post_id):
        pass

    @abstractmethod
    def get_posts_reacted_by_user(self)-> List[int]:
        pass
    
    @abstractmethod
    def get_post_details_dto(self, post_id: int) -> PostCompleteDetailsDto:
        pass
