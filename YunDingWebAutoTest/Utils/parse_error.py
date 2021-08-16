"""
AUTHOR: Seamus
DATE: 2020/09/14
DESCRIPTION:
"""

ERR_ALL_SUCCESS = 0
ERR_EXIST_FAILED = 1
ERR_INTERRUPTED = 2
ERR_INTERNAL_ERROR = 3
ERR_WRONG_CMD_USAGE = 4
ERR_NO_CASE_FILE_FOUND = 5


def get_error(err_code):
    """
    Exit code 0 所有用例执行完毕，全部通过
    Exit code 1 所有用例执行完毕，存在Failed的测试用例
    Exit code 2 用户中断了测试的执行
    Exit code 3 测试执行过程发生了内部错误
    Exit code 4 pytest 命令行使用错误
    Exit code 5 未采集到可用测试用例文件
    :param err_code:  即exit code
    :return: error reason
    """
    if err_code == ERR_ALL_SUCCESS:
        return '所有用例执行完毕，全部通过'
    elif err_code == ERR_EXIST_FAILED:
        return '所有用例执行完毕，存在Failed的测试用例'
    elif err_code == ERR_INTERRUPTED:
        return '用户中断了测试的执行'
    elif err_code == ERR_INTERNAL_ERROR:
        return '测试执行过程发生了内部错误'
    elif err_code == ERR_WRONG_CMD_USAGE:
        return 'pytest命令行使用错误'
    elif err_code == ERR_NO_CASE_FILE_FOUND:
        return '未采集到可用测试用例文件'
    else:
        return '未知错误'
