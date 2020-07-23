import pytest
from fb_post_v2.interactors.storages.storage_interface import \
    StorageInterface

from fb_post_v2.interactors.storages.dtos import *
from fb_post_v2.constants.enums import ReactionType

import datetime

@pytest.fixture
def user_dtos():
    user_dtos = [UserDto(
        user_id =1,
        name = "usha",
        profile_pic ="www.gmail.com"
        )]
    return user_dtos
@pytest.fixture        
def reaction_dtos():
    reaction_dtos = [ReactionTypeDto(
        reaction_type = "WOW"
        )]
    return reaction_dtos
    
@pytest.fixture
def post_dto():
    post_dto = [PostDto(
        user_id =1,
        post_id =1,
        post_content = "ammu",
        pub_date_time = "22-12-13"
        )]
    return post_dto
    
@pytest.fixture
def comment_dtos():
    comment_dtos = [CommentDto(
        comment_id = 1,
        post_id =1,
        user_id = 1,
        comment_content = "usha",
        pub_date_time = "22-12-1996",
        parent_comment = 1)]
    return comment_dtos














































