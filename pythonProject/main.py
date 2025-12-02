import copy
openapi_json = {
    "openapi": "3.1.0",
    "info": {
        "title": "FastAPI",
        "version": "0.1.0"
    },
    "paths": {
        "/": {
            "get": {
                "summary": "Root",
                "operationId": "root__get",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/APIResponse"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/auth/login": {
            "post": {
                "tags": [
                    "auth"
                ],
                "summary": "Authenticate User",
                "description": "Log in a user by validating their email and password.",
                "operationId": "authenticateUser",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/LoginRequest"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {
                        "description": "User successfully authenticated.",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/StandardResponse"
                                },
                                "examples": {
                                    "successResponse": {
                                        "value": {
                                            "success": True,
                                            "message": "User logged in successfully.",
                                            "data": {
                                                "userId": "12345",
                                                "accessToken": "abc123"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation error occurred.",
                        "content": {
                            "application/json": {
                                "examples": {
                                    "validationErrorResponse": {
                                        "value": {
                                            "success": False,
                                            "message": "Validation error: email or password is incorrect."
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/crawl_by_guname": {
            "get": {
                "summary": "Crawl By Guname",
                "operationId": "crawl_by_guname_crawl_by_guname_get",
                "parameters": [
                    {
                        "name": "guname",
                        "in": "query",
                        "required": False,
                        "schema": {
                            "type": "string",
                            "default": "영등포구",
                            "title": "Guname"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {

                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/get_article": {
            "post": {
                "summary": "Get Article",
                "operationId": "get_article_get_article_post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "title": "Filter Condition List"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {

                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/test_get_dongname_list": {
            "get": {
                "summary": "Test Get Dongname List",
                "operationId": "test_get_dongname_list_test_get_dongname_list_get",
                "parameters": [
                    {
                        "name": "guname",
                        "in": "query",
                        "required": True,
                        "schema": {
                            "type": "string",
                            "title": "Guname"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {

                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/get_articles": {
            "get": {
                "summary": "Get Articles",
                "operationId": "get_articles_get_articles_get",
                "parameters": [
                    {
                        "name": "gu",
                        "in": "query",
                        "required": True,
                        "schema": {
                            "type": "string",
                            "description": "정렬 기준 (예: deposit_fee_asc)",
                            "title": "Gu"
                        },
                        "description": "정렬 기준 (예: deposit_fee_asc)"
                    },
                    {
                        "name": "dong",
                        "in": "query",
                        "required": False,
                        "schema": {
                            "anyOf": [
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "null"
                                }
                            ],
                            "description": "동 이름 (선택 사항)",
                            "title": "Dong"
                        },
                        "description": "동 이름 (선택 사항)"
                    },
                    {
                        "name": "deposit_min",
                        "in": "query",
                        "required": True,
                        "schema": {
                            "type": "integer",
                            "description": "최소 보증금",
                            "title": "Deposit Min"
                        },
                        "description": "최소 보증금"
                    },
                    {
                        "name": "deposit_max",
                        "in": "query",
                        "required": False,
                        "schema": {
                            "type": "integer",
                            "description": "최대 보증금",
                            "title": "Deposit Max"
                        },
                        "description": "최대 보증금"
                    },
                    {
                        "name": "rent_min",
                        "in": "query",
                        "required": True,
                        "schema": {
                            "type": "integer",
                            "description": "최소 월세",
                            "title": "Rent Min"
                        },
                        "description": "최소 월세"
                    },
                    {
                        "name": "rent_max",
                        "in": "query",
                        "required": False,
                        "schema": {
                            "type": "integer",
                            "description": "최대 월세",
                            "title": "Rent Max"
                        },
                        "description": "최대 월세"
                    },
                    {
                        "name": "area_min",
                        "in": "query",
                        "required": False,
                        "schema": {
                            "type": "integer",
                            "description": "최소 면적",
                            "title": "Area Min"
                        },
                        "description": "최소 면적"
                    },
                    {
                        "name": "area_max",
                        "in": "query",
                        "required": False,
                        "schema": {
                            "type": "integer",
                            "description": "최대 면적",
                            "title": "Area Max"
                        },
                        "description": "최대 면적"
                    },
                    {
                        "name": "article_class",
                        "in": "query",
                        "required": True,
                        "schema": {
                            "type": "string",
                            "description": "매물 종류",
                            "title": "Article Class"
                        },
                        "description": "매물 종류"
                    },
                    {
                        "name": "cursor",
                        "in": "query",
                        "required": True,
                        "schema": {
                            "type": "string",
                            "description": "페이지 번호",
                            "title": "Cursor"
                        },
                        "description": "페이지 번호"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {

                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/folder/create": {
            "post": {
                "summary": "Create Folder",
                "operationId": "create_folder_folder_create_post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/Body_create_folder_folder_create_post"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {

                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/folder/list": {
            "get": {
                "summary": "Get Folder List",
                "operationId": "get_folder_list_folder_list_get",
                "parameters": [
                    {
                        "name": "user_id",
                        "in": "query",
                        "required": True,
                        "schema": {
                            "type": "string",
                            "description": "사용자 ID",
                            "title": "User Id"
                        },
                        "description": "사용자 ID"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {

                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/folder/add-estate": {
            "post": {
                "summary": "Add Estate To Folder",
                "operationId": "add_estate_to_folder_folder_add_estate_post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/Body_add_estate_to_folder_folder_add_estate_post"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {

                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/folder/{user_id}/{folder_name}": {
            "get": {
                "summary": "Get Estates In Folder",
                "operationId": "get_estates_in_folder_folder__user_id___folder_name__get",
                "parameters": [
                    {
                        "name": "user_id",
                        "in": "path",
                        "required": True,
                        "schema": {
                            "type": "string",
                            "title": "User Id"
                        }
                    },
                    {
                        "name": "folder_name",
                        "in": "path",
                        "required": True,
                        "schema": {
                            "type": "string",
                            "title": "Folder Name"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {

                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/folder/remove-estate": {
            "post": {
                "summary": "Remove Estate From Folder",
                "operationId": "remove_estate_from_folder_folder_remove_estate_post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/Body_remove_estate_from_folder_folder_remove_estate_post"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {

                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/folder/delete/{user_id}/{folder_name}": {
            "delete": {
                "summary": "Delete Folder",
                "operationId": "delete_folder_folder_delete__user_id___folder_name__delete",
                "parameters": [
                    {
                        "name": "user_id",
                        "in": "path",
                        "required": True,
                        "schema": {
                            "type": "string",
                            "title": "User Id"
                        }
                    },
                    {
                        "name": "folder_name",
                        "in": "path",
                        "required": True,
                        "schema": {
                            "type": "string",
                            "title": "Folder Name"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {

                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "components": {
        "schemas": {
            "APIResponse": {
                "properties": {
                    "success": {
                        "type": "boolean",
                        "title": "Success"
                    },
                    "message": {
                        "type": "string",
                        "title": "Message"
                    },
                    "data": {
                        "type": "object",
                        "title": "Data"
                    }
                },
                "type": "object",
                "required": [
                    "success",
                    "message",
                    "data"
                ],
                "title": "APIResponse"
            },
            "Body_add_estate_to_folder_folder_add_estate_post": {
                "properties": {
                    "user_id": {
                        "type": "string",
                        "title": "User Id",
                        "description": "사용자 ID"
                    },
                    "folder_name": {
                        "type": "string",
                        "title": "Folder Name",
                        "description": "폴더 이름"
                    },
                    "estate_ids": {
                        "items": {
                            "type": "string"
                        },
                        "type": "array",
                        "title": "Estate Ids",
                        "description": "부동산 ID"
                    }
                },
                "type": "object",
                "required": [
                    "user_id",
                    "folder_name",
                    "estate_ids"
                ],
                "title": "Body_add_estate_to_folder_folder_add_estate_post"
            },
            "Body_create_folder_folder_create_post": {
                "properties": {
                    "user_id": {
                        "type": "string",
                        "title": "User Id",
                        "description": "사용자 ID"
                    },
                    "folder_name": {
                        "type": "string",
                        "title": "Folder Name",
                        "description": "생성할 폴더 이름"
                    }
                },
                "type": "object",
                "required": [
                    "user_id",
                    "folder_name"
                ],
                "title": "Body_create_folder_folder_create_post"
            },
            "Body_remove_estate_from_folder_folder_remove_estate_post": {
                "properties": {
                    "user_id": {
                        "type": "string",
                        "title": "User Id",
                        "description": "사용자 ID"
                    },
                    "folder_name": {
                        "type": "string",
                        "title": "Folder Name",
                        "description": "폴더 이름"
                    },
                    "estate_id": {
                        "type": "string",
                        "title": "Estate Id",
                        "description": "제거할 부동산 ID"
                    }
                },
                "type": "object",
                "required": [
                    "user_id",
                    "folder_name",
                    "estate_id"
                ],
                "title": "Body_remove_estate_from_folder_folder_remove_estate_post"
            },
            "HTTPValidationError": {
                "properties": {
                    "detail": {
                        "items": {
                            "$ref": "#/components/schemas/ValidationError"
                        },
                        "type": "array",
                        "title": "Detail"
                    }
                },
                "type": "object",
                "title": "HTTPValidationError"
            },
            "LoginRequest": {
                "properties": {
                    "email": {
                        "type": "string",
                        "title": "Email",
                        "examples": [
                            "user@example.com"
                        ]
                    },
                    "password": {
                        "type": "string",
                        "title": "Password",
                        "examples": [
                            "securePassword123"
                        ]
                    }
                },
                "type": "object",
                "required": [
                    "email",
                    "password"
                ],
                "title": "LoginRequest"
            },
            "StandardResponse": {
                "properties": {
                    "success": {
                        "type": "boolean",
                        "title": "Success"
                    },
                    "message": {
                        "type": "string",
                        "title": "Message"
                    },
                    "data": {
                        "anyOf": [
                            {
                                "type": "object"
                            },
                            {
                                "type": "null"
                            }
                        ],
                        "title": "Data"
                    }
                },
                "type": "object",
                "required": [
                    "success",
                    "message"
                ],
                "title": "StandardResponse"
            },
            "ValidationError": {
                "properties": {
                    "loc": {
                        "items": {
                            "anyOf": [
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "integer"
                                }
                            ]
                        },
                        "type": "array",
                        "title": "Location"
                    },
                    "msg": {
                        "type": "string",
                        "title": "Message"
                    },
                    "type": {
                        "type": "string",
                        "title": "Error Type"
                    }
                },
                "type": "object",
                "required": [
                    "loc",
                    "msg",
                    "type"
                ],
                "title": "ValidationError"
            }
        }
    }
}


def resolve_ref(obj, components):
    if isinstance(obj, dict):
        if "$ref" in obj:
            ref_path = obj['$ref'].strip('#/').split('/')
            ref = components
            for key in ref_path[1:]:
                if not isinstance(ref, dict) or key not in ref:
                    return obj
                ref = ref[key]
            return resolve_ref(ref, components)
        else:
            return {k: resolve_ref(v, components) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [resolve_ref(item, components) for item in obj]
    else:
        return obj


def parse_openapi_paths_by_id(paths, components, url):
    path_item = paths.get(url, {})
    if not path_item:
        return None

    resolved_path_item = copy.deepcopy(path_item)

    for method, info in resolved_path_item.items():
        if info.get("requestBody"):
            info["requestBody"] = resolve_ref(info["requestBody"], components)
        if info.get("responses"):
            info["responses"] = resolve_ref(info["responses"], components)

    return resolved_path_item


def get_user_operation_by_id(openapi_json, url):
    components = openapi_json.get("components", {})
    result = parse_openapi_paths_by_id(openapi_json.get("paths", {}), components, url)
    print(result)
    return result


get_user_operation_by_id(openapi_json, "/auth/login")
