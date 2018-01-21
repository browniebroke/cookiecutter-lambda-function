def test_run_basic(cookies):
    result = cookies.bake(extra_context={'project_slug': 'lambda_func'})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'lambda_func'
    assert result.project.isdir()
