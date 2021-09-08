### Valython

Valython is Python library for validating string and words for email, password, URL etc. Its a light-weight library and easy to use.

### Installation `[publishing soon]`
#### PyPi Command
Go to [https://pypi.org/project/valython](https://pypi.org/project/valython) or use command
```sh
pip install valython
```

#### Git Command
```sh
git clone https://github.com/rohit-chouhan/valython
```

### Methods
here some methods with example when it will return true, and false.  support length is the parameter which use to give limit of word like - `isString('Rohit', 5)` so it will return true because `Rohit` length is not less then give value `5`.

|method|true|false|support length| description|
|-|-|-|-|-|
|isString()|Rohit| Ro<span style="color:red;">8</span>it| yes| Contain only string|
|isDigits()|56934| 3<span style="color:red;">F</span>53<span style="color:red;">A</span>3| yes|Contain only digits|
|isPassword()|Neha$1234|Neha1234| yes|Check strong password|
|isSymbol()|^$$&#|^$<span style="color:red;">H</span>#$%| yes|Contain only symbols|
|isUrl()|https://rohitchouhan.com|rohitchouhan.com| no| Validate URL|
|isEmail()|neha@gmail.com|neha@.com| no|Validate Email|
|isAnyDigit()| Rohi<span style="color:green;">45</span>Ch@| HRYD$% | no| If found digit in text|
|isAnyString()| <span style="color:green;">Rohit</span>45@| 4356$% | no|If found string in text
|isAnySpace()| Rohit 45 @| Rohit45@ | no| If found space in text|
|isAnySymbol()| Rohit45@| Rohit45Ch | no| If found symbol in text|