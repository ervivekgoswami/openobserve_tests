from utils.config_reader import config

def test_search_api(api_request_context):
    user_email = config['TESTDATA']['username']
    user_password = config['TESTDATA']['password']
    resource_login = config['API_DATA']['resource_login']
    org_id = config['API_DATA']['org_id']
    resource_search = config['API_DATA']['resource_search'].replace('org_id', org_id)

    response_login = api_request_context.post(
        resource_login,
        data={
            "name": user_email,
            "password": user_password
        }
    )
    # Assert response status
    assert response_login.ok, f"Login failed: {response_login.status} {response_login.text()}"
    api_request_context.cookie = response_login.headers.get("set-cookie")
    response_search = api_request_context.post(
        resource_search,
        data={
            "query": {
                "end_time": 1675185660872049,
                "from": 0,
                "size": 10,
                "sql": "SELECT histogram(_timestamp) as 'x_axis_1', count(body_channel) as 'y_axis_1'  FROM 'windows'  GROUP BY x_axis_1 ORDER BY x_axis_1 ASC",
                "start_time": 1675182660872049
            }
        }
    )
    # Assert response status
    assert response_search.ok, f"Search failed: {response_search.status} {response_search.text()}"
