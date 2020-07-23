import pytest
from fb_post_v2.constants.enums import *
from fb_post_v2.dtos.dtos import *
import datetime
@pytest.fixture()
def user_dtos():
    user_dtos = [UserDto(
        user_id = 1,
        name = "sharmila",
        profile_pic="www.google.com"
    )]
    return user_dtos
    
@pytest.fixture()
def reaction_dtos():
    reaction_dtos = [ReactionTypeDto(
        reaction = "LOVE"
        )]
    return reaction_dtos

@pytest.fixture()
def comment_dtos():
    comment_dtos = [CommentDto(
        comment_id = 1,
        commenter = 1,
        comment_content = "Hello",
        commented_at = datetime.datetime.now(),
        parent_comment = None
        )]
    return comment_dtos

@pytest.fixture()
def post_dtos():
    post_dtos = PostDetailsDto(
        post_id=1,
        posted_by=1,
        posted_at=datetime.datetime.now(),
        post_content="Namasthe"
        )
    return post_dtos
@pytest.fixture()
def list_of_post_dtos():
    post_dtos = [PostDetailsDto(
        post_id=1,
        posted_by=1,
        posted_at=datetime.datetime.now(),
        post_content="Namasthe"
        )]
    return post_dtos

@pytest.fixture()
def reactions_dtos():
    reactions_dtos = [ReactionsDto(
        reaction_id=1,
        post_id=1,
        user_id=1,
        reaction_type=ReactionType.LIKE.value,
        comment_id=None
        ),ReactionsDto(
        reaction_id=1,
        post_id=None,
        user_id=1,
        reaction_type=ReactionType.LOVE.value,
        comment_id=1
        )]
    return reactions_dtos
@pytest.fixture()
def reactions_dtos_empty():
    reactions_dtos = [ReactionsDto(
        reaction_id=1,
        post_id=None,
        user_id=1,
        reaction_type=ReactionType.LOVE.value,
        comment_id=1
        )]
    return reactions_dtos
@pytest.fixture()
def reactions_dtos_comments_empty():
    reactions_dtos = [ReactionsDto(
        reaction_id=1,
        post_id=1,
        user_id=1,
        reaction_type=ReactionType.LIKE.value,
        comment_id=None
        )]
    return reactions_dtos

@pytest.fixture()
def post_reactions():
    post_reactions = PostReactionDto(
        post_id=1,
        reaction_type=[ReactionType.LIKE.value],
        reaction_count=1
        )
    return post_reactions
@pytest.fixture()
def empty_post_reactions():
    post_reactions = PostReactionDto(
        post_id=1,
        reaction_type=[],
        reaction_count=0
        )
    return post_reactions

@pytest.fixture()
def comment_replies_dtos():
    replies_dtos = [CommentRepliesDto(
        comment_id=1,
        replies_count=0
        )]
    return replies_dtos
@pytest.fixture()
def comment_reactions():
    comment_reactions = [CommentReactionDto(
        comment_id=1,
        reaction_type=[ReactionType.LOVE.value],
        reaction_count=1
        )]
    return comment_reactions
@pytest.fixture()
def comment_reactions_empty():
    comment_reactions = [CommentReactionDto(
        comment_id=1,
        reaction_type=[],
        reaction_count=0
        )]
    return comment_reactions

@pytest.fixture()
def list_of_post_reactions():
    post_reactions = [PostReactionDto(
        post_id=1,
        reaction_type=[ReactionType.LIKE.value],
        reaction_count=1
        )]
    return post_reactions
@pytest.fixture()
def list_of_post_reactions_empty():
    post_reactions = [PostReactionDto(
        post_id=1,
        reaction_type=[],
        reaction_count=0
        )]
    return post_reactions

@pytest.fixture()
def get_post_response():
    get_post_response = {
        'post_content': 'NEW POST',
        'post_id': 1,
        'posted_at': datetime.datetime.now(),
        'posted_by': {
            'name': 'sharmila',
            'profile_pic': 'www.google.com',
            'user_id': 1
        },
        'reactions': {
            'count': 1,
            'type': [
                'HAHA'
            ]
        },
        'comments': [
            {
                'comment_content': 'nice post',
                'comment_id': 1,
                'commented_at': datetime.datetime.now(),
                'commenter': {
                    'name': 'sharmila',
                    'profile_pic': 'www.google.com',
                    'user_id': 1
                },
                'reactions': {
                    'count': 1,
                    'type': [
                        'SAD'
                    ]
                },
                'replies': [
                    {
                        'comment_content': 'nice post',
                        'comment_id': 2,
                        'commented_at': datetime.datetime.now(),
                        'commenter': {
                            'name': 'sharmila',
                            'profile_pic': 'www.google.com',
                            'user_id': 1
                        }
                    },
                    {
                        'count': 1,
                        'type': [
                            'WOW'
                        ]
                    }
                ],
                'replies_count': 1
            }

        ],
        "comments_count": 1
    }
    return get_post_response

@pytest.fixture()
def get_post_response_with_empty_comment():
    get_post_response = {
        'post_content': 'NEW POST',
        'post_id': 1,
        'posted_at': datetime.datetime.now(),
        'posted_by': {
            'name': 'sharmila',
            'profile_pic': 'www.google.com',
            'user_id': 1
        },
        'reactions': {
            'count': 1,
            'type': [
                'HAHA'
            ]
        },
        'comments': [
            {
                'comment_content': 'nice post',
                'comment_id': 1,
                'commented_at': datetime.datetime.now(),
                'commenter': {
                    'name': 'sharmila',
                    'profile_pic': 'www.google.com',
                    'user_id': 1
                },
                'reactions': {
                    'count': 0,
                    'type': []
                },
                'replies': [
                    {
                        'comment_content': 'nice post',
                        'comment_id': 2,
                        'commented_at': datetime.datetime.now(),
                        'commenter': {
                            'name': 'sharmila',
                            'profile_pic': 'www.google.com',
                            'user_id': 1
                        }
                    },
                    {
                        'count': 1,
                        'type': [
                            'WOW'
                        ]
                    }
                ],
                'replies_count': 1
            }

        ],
        "comments_count": 1
    }
    return get_post_response
    
@pytest.fixture()
def get_post_response_with_empty_post_reactions():
    get_post_response = {
        'post_content': 'NEW POST',
        'post_id': 1,
        'posted_at': datetime.datetime.now(),
        'posted_by': {
            'name': 'sharmila',
            'profile_pic': 'www.google.com',
            'user_id': 1
        },
        'reactions': {
            'count': 0,
            'type': []
        },
        'comments': [
            {
                'comment_content': 'nice post',
                'comment_id': 1,
                'commented_at': datetime.datetime.now(),
                'commenter': {
                    'name': 'sharmila',
                    'profile_pic': 'www.google.com',
                    'user_id': 1
                },
                'reactions': {
                    'count': 1,
                    'type': [
                        'SAD'
                    ]
                },
                'replies': [
                    {
                        'comment_content': 'nice post',
                        'comment_id': 2,
                        'commented_at': datetime.datetime.now(),
                        'commenter': {
                            'name': 'sharmila',
                            'profile_pic': 'www.google.com',
                            'user_id': 1
                        }
                    },
                    {
                        'count': 1,
                        'type': [
                            'WOW'
                        ]
                    }
                ],
                'replies_count': 1
            }

        ],
        "comments_count": 1
    }
    return get_post_response

@pytest.fixture()
def get_user_posts_response():
    get_user_posts_response = [{
        'post_content': 'NEW POST',
        'post_id': 1,
        'posted_at': datetime.datetime.now(),
        'posted_by': {
            'name': 'sharmila',
            'profile_pic': 'www.google.com',
            'user_id': 1
        },
        'reactions': {
            'count': 1,
            'type': [
                'HAHA'
            ]
        },
        'comments': [
            {
                'comment_content': 'nice post',
                'comment_id': 1,
                'commented_at': datetime.datetime.now(),
                'commenter': {
                    'name': 'sharmila',
                    'profile_pic': 'www.google.com',
                    'user_id': 1
                },
                'reactions': {
                    'count': 1,
                    'type': [
                        'SAD'
                    ]
                },
                'replies': [
                    {
                        'comment_content': 'nice post',
                        'comment_id': 2,
                        'commented_at': datetime.datetime.now(),
                        'commenter': {
                            'name': 'sharmila',
                            'profile_pic': 'www.google.com',
                            'user_id': 1
                        }
                    },
                    {
                        'count': 1,
                        'type': [
                            'WOW'
                        ]
                    }
                ],
                'replies_count': 1
            }

        ],
        "comments_count": 1
    }]
    return get_user_posts_response
