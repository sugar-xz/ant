# Welcome to Automated testing tools

## How to use

1. Clone the repo

    ```
    git clone -b master https://github.com/turingvideo/TestAuto.git
    ```

2. Install python packages

    ```
    pip install -r requirements.txt
    ```
3.  Configure the test cases
    The test cases are in the `TestSuite` directory by default.
    
    The test case list is in the `caselist.txt` file by default
    ```
    # Format
    ****:
        - *** + `/` + `case name`
    # example
    basecase:
        TestSuite/case/test_case
    ```

4. run locally

    ```
    python run_test.py
    ```

## Falsk Server

```shell
    python server.py
```

## Test demo

```shell
cd TestSuite/demo
# Including interface, UI automation, etc.
```

##  Environment variable

####    Common environment variable
|  Param   | Default  | note    | attention |
|  ----  | ----  |  ----    | ----  |
| AUTO_LOG_WRITE  | `False` |  If true, save the `log` in the `report` directory   | ** |
| AUTO_SEND_EMAIL  | `False` | Whether to send an email after the test | * |
| AUTO_REPORT_NAME  | `report` | Custom result report name |    |
| AUTO_CASE_FILE  | `caselist.yml` | In the file is a list of test cases that need to be executed | |
| AUTO_CASE_PATH  | `TestSuite` |    Directory for storing test cases    |    |
| AUTO_CASE_SUBSET  | `basecase` |   Test cases executed, multiple parameters are separated by `,`  | ***** |
| AUTO_CSRFTOKEN  | `False` |   Website header to interface test（will deprecated）  |    |
| AUTO_DB  | `postgres` |   Support `posetgrs` and `mysql`   |    |
| API_VERSION  | `v1` |  v{int}}   | * |
| BROWSER_DRIVER  | `None` |  selenium `driver` absolute path   | ****** |

_`AUTO_SEND_EMAIL` need to configure the sending account in `config.ini`_

_`AUTO_CASE_FILE` and `AUTO_CASE_PATH`, Currently only supports the current project directory._

###    Project environment variables

####    MINIBOX
|  Param   | Default  | note    |
|  ----  | ----  |  ----    |
| AUTO_MINIBOX_URL  | `http://127.0.0.1:8000` |  domain:port   |

####    SUPERBOX
|  Param   | Default  | note    |
|  ----  | ----  |  ----    |
| AUTO_SUPERBOX_URL  | `http://127.0.0.1:8000` |  domain:port   |
| API_VERSION  | `v1` |  v{`int`}}   |
