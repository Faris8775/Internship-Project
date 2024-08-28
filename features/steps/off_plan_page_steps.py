from behave import given, when, then




@then('Verify the right page opens')
def verify_off_plan_opens(context):
    context.app.off_plan_page.verify_off_plan_page()


@then('Verify each product on this page contains a title and picture visible')
def verify_each_project_on_off_plan(context):
    context.app.off_plan_page.verify_each_product_on_off_plan()