import pytest

pytest.main(["-m smoke","--junitxml=HtmlReport/test_report.xml","--html=HtmlReport/test_report.html"])