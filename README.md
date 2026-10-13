# RU

## Цель

Программа составляет запись логической функции в СДНФ, СКНФ и в виде полинома Жегалкина по её двоичному значению. Больше не придётся вручную составлять таблицы истинности и записывать эти формы по алгоритмам, программа сделает это за вас.

## Как пользоваться

Для построения программой всех трёх форм записи логической функции нужно: 
1. Ввести количество используемых переменных для высказываний. 
2. Ввести двоичное значение функции. 

```Длина значения функции = 2^(кол-во переменных)```. 

Если вы введёте **"3"** в качестве количества переменных, а в значение функции введёте строку из более чем **восьми** символов, то они будут отсечены.

### Пример
> | x   | y   | f(x,y) |
> | --- | --- | ------ |
> | 0   | 0   | **1**  |
> | 0   | 1   | **0**  |
> | 1   | 0   | **1**  |
> | 1   | 1   | **1**  |

1. Вводим количество переменных, у нас это **2**
2. Вводим значение функции, у нас это **1011**

Для построения нам необходимо знать лишь столбец **f(x,y)**. Дальше программа составит всё сама.

В выводе программы получаем:
```
СДНФ: x̄₀x̄₁ ∨ x₀x̄₁ ∨ x₀x₁

СКНФ: (x₀∨x₁)

Полином Жегалкина: 1 ⊕ x₁ ⊕ x₀x₁
```
Абсолютно верное построение.

---
**Всё! Приятного пользования.**
<br>
<br>
<br>
 # EN

## Purpose

The program generates the PDNF (Principal Disjunctive Normal Form), PCNF (Principal Conjunctive Normal Form), and the Zhegalkin polynomial of a logical function based on its binary value. You no longer have to manually build truth tables and write out these forms using algorithms—the program will do it all for you.

## How to use

To generate all three forms of a logical function, you need to: 
1. Enter the number of variables used for the propositions. 
2. Enter the binary value of the function. 

```Function value length = 2^(number of variables)```. 

If you enter **"3"** as the number of variables, and enter a string of more than **eight** characters as the function value, the extra characters will be cut off.

### Example
> | x   | y   | f(x,y) |
> | --- | --- | ------ |
> | 0   | 0   | **1**  |
> | 0   | 1   | **0**  |
> | 1   | 0   | **1**  |
> | 1   | 1   | **1**  |

1. Enter the number of variables, which is **2** in our case.
2. Enter the function value, which is **1011** in our case.

To build the forms, you only need to know the **f(x,y)** column. The program will handle the rest on its own.

The program output will look like this:
```
PDNF: x̄₀x̄₁ ∨ x₀x̄₁ ∨ x₀x₁

PCNF: (x₀∨x₁)

Zhegalkin polynomial: 1 ⊕ x₁ ⊕ x₀x₁
```
An absolutely correct generation.

---
**That's it! Enjoy using the program.**
