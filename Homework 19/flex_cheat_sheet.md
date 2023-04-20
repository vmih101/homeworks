# Краткий конспект по флексу
***
## display: flex;
```
.container{
    display: flex;  
}
```
Определяет, что данный контейнер получает параметр flex и определяет все его дочерние элементы  
как элементы этого flex контейнера. Также существует параметр inline-flex. Их отличия  
в том, как буде вести элемент на странице по отношению к другим элементам, как блочный  
или строчный.
***
## order
```
.item{
    order: 5;
}
```
Данный атрибут позволяет задать в каком порядке будет отображаться определнный элемент  
во флекс-контейнере  
По умолчанию располагаются в исходном порядке, то есть в порядке написания в html документе.
***
## flex-direction
```
.container {
    flex-direction: row | row-reverse | column | column-reverse;
}
```
Задаёт в каком направлении будут располагаться элементы в контейнере.
* row - в горизонтальном направлении слева направо
* row-reverse - в горизонтальном направлении справа налево
* column - в вертикальном направлении сверху вниз
* column-reverse - в вертикальном направлении снизу вверх
## flex-wrap
```
.container {
    flex-wrap: nowrap | wrap | wrap-reverse;
}
```
Позволяет переносить элементы на новые строки/колонки. По-умолчанию элементы находится на одной линии, и уменьшаются в  
размере, в случае если не могут вместиться в исходном размере.
* wrap - элементы переносятся на новую строку/колонку при необходимости
* wrap-reverse - элементы переносятся на новую строку и изменяется их порядок
***
## flex-flow
```
.container {
    flex-flow: column wrap;
}
```
Позволяет задать значения flex-direction и flex-wrap в одном параметре, так зачастую они используются вместе. Первым  
задаётся значения для flex-direction (row, row-reverse, column, column-reverse), затем для flex-wrap (nowrap, wrap,  
wrap-reverse)
***
## justify-content
```
.container {
    justify-content: flex-start | flex-end | center | space-between | space-around | space-evenly | start | end | left  
    | right ... + safe | unsafe;
}
```
Задаёт выравнивание элементов контейнера по горизонтальной оси.
* flex-start: элементы размещаются в начале контейнера
* flex-end: элементы размещаются в конце контейнера
* center: элементы размещаются по центру контейнера
* space-between: элементы размещаются равномерно по всей длине контейнера, первый и последний элемент находятся по краям
контейнера
* space-around: элементы размещаются равномерно по всей длине контейнера, при этом для каждого элемента определятся 
равное по размеру пустое пространство с обеих сторон и не учитывается пустое пространство вокруг следующего элемента.
Пример: в контейнере имеется два элемента, применён параметр space-around, у каждого элемента space-around составил 
500px, то есть расстояние от левого края до первого контейнера и от правого края до второго контейнера составляет 500px,
расстояние между контейнерами составит 1000px, так как каждый имеет собственный space-around 500px, что в сумме и даёт 
1000px.
* space-evenly: визуально может показаться, что не имеет отличий от space-around, но фактически при применении этого
параметра рассчитывается равное пространство между элементами и краями контейнера, все эти отрезки будут иметь 
одинаковое значение. 
***
## align-items
Задаёт выравнивание элементов контейнера по вертикальной оси.
```
.container {
    align-items: stretch | flex-start | flex-end | center | baseline | first baseline | last baseline | start | end |
    self-start | self-end + ... safe | unsafe;
}
```
* stretch (по умолчанию): растягивает элементы по вертикальной оси, с учётом высоты родительского контейнера.
* flex-start / start / self-start: элементы располагаются в начале (сверху) контейнера.
* flex-end / end / self-end: элементы располагаются в конце (внизу) контейнера.
* center: элементы располагаются в центре контейнера.
* baseline: элементы располагаются по базовой линии содержимого элементов. Другими словами учитывается выравнивание 
содержимого внутри каждого элемента, содержимое контейнеров будет находиться на одной линии.
***
## align-content
Данный параметр работает только в том случае, когда элементы располагаются в несколько строк/колонок
(flex-wrap: wrap | wrap-reverse). Определяет расположение строк или колонок внутри контейнера.
```
.container {
    align-content: flex-start | flex-end | center | space-between | space-around | space-evenly | stretch | start 
    | end | baseline | first baseline | last baseline + ... safe | unsafe;
}
```
* flex-start / start: строки располагаются в начале контейнера.
* flex-end / end: строки располагаются в конце контейнера.
* center: строки располагаются в центре контейнера.
* space-between: равное расстояние между строками, первая строка в начале контейнера, последняя - в конце.
* space-around: равное расстояние с каждой стороны строки.
* space-evenly: равное расстояние между строками.
* stretch: строки растягиваются таким образом, чтобы занять всё пространство контейнера.
***
## gap, row-gap, column-gap
Задаёт расстояние между элементами контейнера, а также строками и колонками.
```
.container {
    display: flex;
    ...
    gap: 10px;
    gap: 10px 20px; /* row-gap column gap */
    row-gap: 10px;
    column-gap: 20px;
}
```
## flex-grow
Определяет способность элементов растягиваться исходя из пропорций.
```
.item {
  flex-grow: 4; /* default 0 */
}
```
Например, если установлено значение 1 для всех элементов, то они будут иметь одинаковые размеры и равномерно займут всё 
свободное место в контейнере. Если для какого-то элемента установить значение 2, то он будет иметь размер в двое больший.
***
## flex-shrink
Определяет способность элементов сжиматься исходя из пропорций, в случае когда в совокупности элементы имеют больший 
размер, чем размер контейнера. Пропорции в данном случае, здесь работают в обратную сторону по сравнению с flex-grow.
Например, если flex-shrink элемента имеет значение 3, то он будет иметь размер в три раза меньший, чем остальные 
элементы в контейнере.
```
.item {
  flex-shrink: 3; /* default 1 */
}
```
## align-self
Позволяет задать выравнивание, для одного определенного элемента в контейнере.
```
.item {
  align-self: auto | flex-start | flex-end | center | baseline | stretch;
}
```





