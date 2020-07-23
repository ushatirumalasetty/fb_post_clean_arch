from dataclasses import dataclass
from fb_post_v2.constants.enums import ReactionType
from datetime import datetime
from typing import Optional,List

@dataclass
class ReactionMetricesDto:
    reaction_type: ReactionType
    count: int

@dataclass()
class UserDto:
    user_id: int
    name: str
    profile_pic: str

@dataclass()
class ReactionTypeDto:
    reaction_type : ReactionType 

@dataclass()
class ReactionDto:
    reaction_id: int
    comment_id: Optional[int]
    post_id: Optional[int]
    user_id: int
    reaction_type: ReactionType

@dataclass
class PostTotalDetailsDto:
    post_id : int
    posted_by: int
    posted_at: datetime
    post_content : str
    
    
    
@dataclass()
class PostReactionCompleteDetailsDto:
    user_dtos: List[UserDto]
    reaction_dtos: List[ReactionDto]


@dataclass()
class CommentDto:
    comment_id: int
    user_id: int
    post_id: Optional[int]
    comment_content: str
    pub_date_time: datetime
    parent_comment: Optional


@dataclass()
class CommentRepliesDto:
    users_dto: List[UserDto]
    comments_dto: List[CommentDto]


@dataclass()
class PostDto:
    user_id: int
    post_content: str
    post_id: int
    pub_date_time: datetime


@dataclass()
class PostCompleteDetailsDto:
    post_dto: List[PostTotalDetailsDto]
    users_dto: List[UserDto]
    comment_dto: List[CommentDto]
    reaction_dto: List[ReactionDto]

@dataclass()
class PostDetailsDto:
    users_dto: List[UserDto]
    post_dto: PostDto
    comments_dto: List[CommentDto]
    reactions_dto: List[ReactionDto]


@dataclass()
class PostReactionDto:
    post_id: int
    reaction_types: ReactionType
    reactions_count: int

@dataclass()
class CommentReactionDto:
    comment_id: int
    reaction_types: ReactionType
    reactions_count: int


@dataclass()
class CommentReplyDto:
    comment_id: int
    reply_count: int

