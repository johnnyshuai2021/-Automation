# -*- coding:UTF-8 -*-
"""
AUTHOR: Zhong xinqi
DATE: 2020/08/06 Thu
DESCRIPTION:检查项管理模块页面元素
"""

import allure
from PageObj.page_base import BasePage
from selenium.webdriver.common.by import By


class CheckList(BasePage):
    shop_management_loc = (By.XPATH, "//*[contains(text(), '巡店管理')]")
    check_management_loc = (By.CSS_SELECTOR, r"#巡店管理\$Menu>li:nth-child(6)")
    create_template_loc = (By.CSS_SELECTOR, ".filter-bar>button:nth-child(4)")  # 新建模板按钮
    template1_name_loc = (
        By.CSS_SELECTOR, ".ant-col.ant-form-item-control-wrapper>div.ant-form-item-control>span>input")  # 模板名称输入框
    submit_template_loc = (By.CSS_SELECTOR, "[type='submit']")  # 创建按钮
    template_list_name_loc = (By.CSS_SELECTOR, ".ant-table-row-cell-break-word")  # 任务列表页面模板名称
    mark_template_loc = (By.CSS_SELECTOR, "#new_Templates_markStrategy>label:nth-child(2)")  # 评分按钮
    template_percent_loc = (By.CSS_SELECTOR, ".ant-input-number-input")  # 阈值输入框
    detail_template_percent_loc = (By.CSS_SELECTOR, ".ant-input-number-input-wrap>input")  # 详情阈值输入框
    points_template_loc = (By.CSS_SELECTOR, "#new_Templates_markStrategy>label:nth-child(1)")  # 扣分按钮
    close_button_loc = (By.CSS_SELECTOR, ".anticon.anticon-close.ant-modal-close-icon")  # 关闭模板说明弹窗按钮
    back_button_loc = (By.CSS_SELECTOR, ".return-back-btn")  # 模板详情返回按钮
    edit_button_loc = (By.CSS_SELECTOR, ".ant-btn.ant-btn-link")  # 模板详情页面编辑按钮
    cancel_edit_button_loc = (By.CSS_SELECTOR, "div.ant-modal-footer>div>button:nth-child(1)")  # 取消编辑按钮
    confirm_edit_button_loc = (By.CSS_SELECTOR, "div.ant-modal-footer>div>button:nth-child(2)")  # 确认编辑按钮
    detail_template_name_loc = (By.CSS_SELECTOR, "div.template-name-bar-left>div:nth-child(2)")  # 模板详情页面模板名称
    detail_template_catefory_list_loc = (By.CSS_SELECTOR, ".tree-node-name.node-width")  # 模板详情分类名称列表，定位一组元素
    detail_scoring_list_loc = (By.CSS_SELECTOR, ".list-content")  # 模板详情评分项名称列表，定位一组元素
    add_classification_loc = (By.CSS_SELECTOR, ".template-name-bar-right>button:nth-child(1)")  # 添加分类按钮
    add_scoring_items_loc = (By.CSS_SELECTOR, ".template-name-bar-right>button:nth-child(2)")  # 添加评分项按钮
    description_loc = (By.CSS_SELECTOR, "#addEditTemplate_name")  # 分类描述输入框
    cancel_loc = (By.CSS_SELECTOR, ".ant-modal-footer>div>button:nth-child(1)")  # 对话框取消按钮
    confirm_loc = (By.CSS_SELECTOR, ".ant-modal-footer>div>button:nth-child(2)")  # 对话框确认按钮
    close_loc = (By.CSS_SELECTOR, ".ant-modal-close-x")  # 关闭对话框按钮
    classification_box_loc = (By.CSS_SELECTOR, ".ant-select-selection__rendered")  # 上级分类下拉框
    open_classification_box_loc = (
        By.CSS_SELECTOR, ".ant-select-tree-switcher.ant-select-tree-switcher_close")  # 下拉框三角形按钮
    classification_title_loc = (By.CSS_SELECTOR, ".ant-select-tree-treenode-switcher-close")  # 分类下拉框内容
    point_content_loc = (By.CSS_SELECTOR, ".ant-form-item-children>#addEditTemplate_name")  # 评分项内容输入框
    score_loc = (By.CSS_SELECTOR, ".ant-input-affix-wrapper>input")  # 分值输入框
    template_detail_loc = (By.XPATH, "//span[text()='详情']")  # 详情按钮,方法需要定位一组元素
    detail_point_loc = (By.CSS_SELECTOR, '.ant-radio-wrapper>.ant-radio')  # 详情编辑页面扣分模板按钮
    detail_mark_loc = (
        By.CSS_SELECTOR, '#addEditTemplate_markStrategy > label:nth-child(2) > span.ant-radio')  # 详情编辑页面评分模板按钮
    delete_template_loc = (By.XPATH, "//span[text()='删除']")  # 删除按钮，方法需要定位一组元素
    confirm_delete_template_loc = (By.CSS_SELECTOR, ".ant-btn.ant-btn-danger")  # 确认删除模板按钮
    cancel_delete_template_loc = (By.CSS_SELECTOR, "div.ant-modal-confirm-btns>button:nth-child(1)")  # 取消删除模板按钮
    template_name_loc = (By.CSS_SELECTOR, "td.ant-table-row-cell-break-word")  # 模板名称，方法需要定位一组元素
    select_template_status_loc = (By.CSS_SELECTOR, "div.ant-select-selection__rendered")  # 模板状态选择框按钮
    select_points_status_loc = (By.CSS_SELECTOR, "[role='listbox']>li:nth-child(3)")  # 状态筛选扣分模板
    select_mark_status_loc = (By.CSS_SELECTOR, "[role='listbox']>li:nth-child(2)")  # 状态筛选评分模板
    select_all_status_loc = (By.CSS_SELECTOR, "[role='listbox']>li:nth-child(2)")  # 状态筛选全部模板
    search_template_loc = (By.CSS_SELECTOR, ".ant-input")  # 搜索模板输入框
    search_template_button_loc = (By.CSS_SELECTOR, ".filter-bar>button:nth-child(3)")  # 查询按钮
    import_template_button_loc = (By.CSS_SELECTOR, ".filter-bar>button:nth-child(5)")  # 导入模板按钮

    @allure.step("点击添加分类按钮")
    def click_add_classification(self):
        self.find_element(*self.add_classification_loc).click()

    @allure.step("点击扣分模式")
    def click_detail_point(self):
        self.find_element(*self.detail_point_loc).click()

    @allure.step("获取模板详情所有分类内容")
    def get_detail_template_catefory_list(self):
        catefory_list = self.find_elements(*self.detail_template_catefory_list_loc)
        name = [i.text.split(' ')[1] for i in catefory_list]
        return name

    @allure.step("获取模板详情所有评分项内容")
    def get_detail_scoring_list(self):
        scoring_list = self.find_elements(*self.detail_scoring_list_loc)
        name = [i.text for i in scoring_list]
        return name

    @allure.step("获取任务列表模板名称")
    def get_template_list_name(self):
        scoring_list = self.find_elements(*self.template_list_name_loc)
        name = [i.text for i in scoring_list]
        return name

    @allure.step("点击评分模式")
    def click_detail_mark(self):
        self.find_element(*self.detail_mark_loc).click()

    @allure.step("点击添加评分项按钮")
    def click_add_scoring_items(self):
        self.find_element(*self.add_scoring_items_loc).click()

    @allure.step("点击对话框取消按钮")
    def click_cancel(self):
        self.find_element(*self.cancel_loc).click()

    @allure.step("点击对话框确认按钮")
    def click_confirm(self):
        self.find_element(*self.confirm_loc).click()

    @allure.step("点击关闭对话框按钮")
    def click_close(self):
        self.find_element(*self.close_loc).click()

    @allure.step("点击分类下拉框")
    def click_classification_box(self):
        self.find_element(*self.classification_box_loc).click()

    @allure.step("点击展开分类按钮")
    def click_open_classification_box(self):
        self.find_element(*self.open_classification_box_loc).click()

    @allure.step("选择一个分类")
    def click_classification_title(self):
        self.find_element(*self.classification_title_loc).click()

    @allure.step("输入评分项内容")
    def input_point_content(self, content):
        self.send_key(content, *self.point_content_loc, clear=True)

    @allure.step("输入分值")
    def input_score(self, score):
        self.send_key(score, *self.score_loc, clear=True)

    @allure.step("输入分类描述")
    def input_description(self, description):
        self.send_key(description, *self.description_loc, clear=True)

    @allure.step("点击巡店管理菜单")
    def click_shop_management(self):
        self.find_element(*self.shop_management_loc).click()

    @allure.step("点击检查项管理")
    def click_check_management(self):
        self.find_element(*self.check_management_loc).click()

    @allure.step("点击新建模板")
    def click_create_template(self):
        self.find_element(*self.create_template_loc).click()

    @allure.step("输入模板名称")
    def input_template_name(self, name):
        self.send_key(name, *self.template1_name_loc, clear=True)

    @allure.step("点击创建按钮")
    def click_submit_template(self):
        self.find_element(*self.submit_template_loc).click()

    @allure.step("点击扣分模式")
    def click_points_template(self):
        self.find_element(*self.points_template_loc).click()

    @allure.step("点击评分模式")
    def click_mark_template(self):
        self.find_element(*self.mark_template_loc).click()

    @allure.step("输入整改阈值")
    def input_template_percent(self, percent):
        self.send_key(percent, *self.template_percent_loc)

    @allure.step("编辑模板输入整改阈值")
    def input_detail_template_percent(self, percent):
        self.send_key(percent, *self.detail_template_percent_loc, clear=True)

    @allure.step("点击说明弹窗关闭按钮")
    def click_close_button1(self):
        self.find_element(*self.close_button_loc).click()

    @allure.step("点击模板详情返回按钮")
    def click_back_button(self):
        self.find_element(*self.back_button_loc).click()

    @allure.step("寻找模板详情关闭按钮,找到就点击")
    def click_close_button(self, tag_params):
        # print('当前时间：{}'.format(datetime.datetime.now()))
        try:
            if tag_params['closeTag'] == 0:
                print('初次进入详情，点击关闭')
                self.find_element(*self.close_button_loc).click()
                tag_params['closeTag'] = 1
        except BaseException:
            print('已点击过关闭，无需点击')

    @allure.step("删除第一个模板")
    def click_delete_template(self):
        delete_buttons = self.find_elements(*self.delete_template_loc)
        delete_buttons[0].click()

    @allure.step("点击第一个模板详情按钮")
    def click_template_detail(self):
        detail_buttons = self.find_elements(*self.template_detail_loc)
        detail_buttons[0].click()

    @allure.step("点击确认删除模板")
    def click_confirm_delete_template(self):
        self.find_element(*self.confirm_delete_template_loc).click()

    @allure.step("点击取消删除模板")
    def click_cancel_delete_template(self):
        self.find_element(*self.cancel_delete_template_loc).click()

    @allure.step("获取第一个模板名称")
    def get_template_name(self):
        names = self.find_elements(*self.template_name_loc)
        content = names[0].text
        return content

    @allure.step("获取详情页模板名称")
    def get_detail_template_name(self):
        name = self.find_element(*self.detail_template_name_loc).text
        return name

    @allure.step("点击筛选栏模板下拉框")
    def click_select_template_status(self):
        self.find_element(*self.select_template_status_loc).click()

    @allure.step("选择扣分模式")
    def click_select_points_status(self):
        self.find_element(*self.select_points_status_loc).click()

    @allure.step("选择评分模式")
    def click_select_mark_status(self):
        self.find_element(*self.select_mark_status_loc).click()

    @allure.step("选择全部模式")
    def click_select_all_status(self):
        self.find_element(*self.select_all_status_loc).click()

    @allure.step("输入模板名称")
    def input_search_template(self, name):
        self.send_key(name, *self.search_template_loc)

    @allure.step("点击查询按钮")
    def click_search_template_button(self):
        self.find_element(*self.search_template_button_loc).click()

    @allure.step("点击导入模板")
    def click_import_template_button(self):
        self.find_element(*self.import_template_button_loc).click()

    @allure.step("点击取消编辑按钮")
    def click_cancel_edit(self):
        self.find_element(*self.cancel_edit_button_loc).click()

    @allure.step("点击确认编辑按钮")
    def click_confirm_edit(self):
        self.find_element(*self.confirm_edit_button_loc).click()

    @allure.step("点击编辑按钮")
    def click_edit_button(self):
        self.find_element(*self.edit_button_loc).click()
