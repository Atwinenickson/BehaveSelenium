# import time

# from behave import when, then, given
# from models.pageobject.actions.coccoc_browser_actions import CocCocBrowserActions, CocCocHomePageActions, \
#     CocCocBottomMenuActions, CocCocPageMenuActions, CocCocMusicPageActions

# coccoc_browser_actions = CocCocBrowserActions()
# coccoc_home_page_actions = CocCocHomePageActions()
# coccoc_bottom_menu_actions = CocCocBottomMenuActions()
# coccoc_page_menu_actions = CocCocPageMenuActions()
# coccoc_music_page_actions = CocCocMusicPageActions()


# @when(u'Go over welcome pages')
# def step_impl(context):
#     coccoc_browser_actions.tap_accept_button(context.browser)
#     coccoc_browser_actions.tap_next_button(context.browser)
#     time.sleep(1)
#     coccoc_browser_actions.tap_next_button(context.browser)

#     coccoc_browser_actions.tap_start_browsing_button(context.browser)


# @then(u'Search box appear')
# def step_impl(context):
#     assert coccoc_home_page_actions.coccoc_search_box_is_displayed(context.browser) is True


# @then(u'Skip notification for coccoc game and coccoc music')
# def step_impl(context):
#     context.browser.back()
#     time.sleep(1)
#     context.browser.back()
#     time.sleep(1)


# @given(u'Choose bottom page menu button')
# def step_impl(context):
#     coccoc_bottom_menu_actions.tap_coccoc_bottom_settings_menu_button(context.browser)


# @when(u'Choose "{option_name}"')
# def step_impl(context, option_name):
#     coccoc_bottom_menu_actions.tap_coccoc_bottom_settings_option(context.browser, option_name)


# @then(u'Choose "{option_name}" from show all tabs')
# def step_impl(context, option_name):
#     coccoc_bottom_menu_actions.tap_coccoc_bottom_shown_tabs_btn(context.browser)
#     coccoc_page_menu_actions.tap_coccoc_page_menu_more_options_btn(context.browser)
#     coccoc_page_menu_actions.tap_coccoc_options_in_more_options_list(context.browser, option_name)
