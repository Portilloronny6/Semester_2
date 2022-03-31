from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_no_goods()
        self.should_be_lbl_basket_is_empty()

    def should_be_no_goods(self):
        assert self.is_not_element_present(*BasketPageLocators.LBL_GOODS_IN_BASKET)

    def should_be_lbl_basket_is_empty(self):
        assert self.browser.find_element(*BasketPageLocators.LBL_BASKET_IS_EMPTY).text == "Your basket is empty. " \
                                                                                          "Continue shopping"
