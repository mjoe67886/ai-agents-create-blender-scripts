# Socket ROTATION


### Methods

- [abs](#abs)
- [add](#add)
- [ceil](#ceil)
- [cos](#cos)
- [cross](#cross)
- [distance](#distance)
- [divide](#divide)
- [dot](#dot)
- [faceforward](#faceforward)
- [floor](#floor)
- [frac](#frac)
- [length](#length)
- [max](#max)
- [min](#min)
- [mod](#mod)
- [multiply](#multiply)
- [multiply_add](#multiply_add)
- [normalize](#normalize)
- [project](#project)
- [reflect](#reflect)
- [refract](#refract)
- [scale](#scale)
- [sin](#sin)
- [snap](#snap)
- [subtract](#subtract)
- [tan](#tan)
- [vector_curves](#vector_curves)
- [wrap](#wrap)

## Methods

### abs


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def abs(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, operation='ABSOLUTE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### add


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def add(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='ADD', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### ceil


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def ceil(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, operation='CEIL', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### cos


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def cos(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, operation='COSINE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### cross


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def cross(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='CROSS_PRODUCT', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### distance


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def distance(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='DISTANCE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### divide


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def divide(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='DIVIDE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### dot


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def dot(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='DOT_PRODUCT', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### faceforward


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- node_label : None
- node_color : None

#### Source code

``` python
def faceforward(self, vector=None, vector_1=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, vector_2=vector_1, operation='FACEFORWARD', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### floor


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def floor(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, operation='FLOOR', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### frac


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def frac(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, operation='FRACTION', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### length


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def length(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, operation='LENGTH', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### max


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def max(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='MAXIMUM', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### min


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def min(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='MINIMUM', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### mod


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def mod(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='MODULO', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### multiply


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def multiply(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='MULTIPLY', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### multiply_add


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- node_label : None
- node_color : None

#### Source code

``` python
def multiply_add(self, vector=None, vector_1=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, vector_2=vector_1, operation='MULTIPLY_ADD', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### normalize


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def normalize(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, operation='NORMALIZE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### project


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def project(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='PROJECT', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### reflect


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def reflect(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='REFLECT', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### refract


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- scale : None
- node_label : None
- node_color : None

#### Source code

``` python
def refract(self, vector=None, scale=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, scale=scale, operation='REFRACT', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### scale


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- scale : None
- node_label : None
- node_color : None

#### Source code

``` python
def scale(self, scale=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, scale=scale, operation='SCALE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### sin


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def sin(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, operation='SINE', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### snap


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def snap(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='SNAP', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### subtract


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- node_label : None
- node_color : None

#### Source code

``` python
def subtract(self, vector=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, operation='SUBTRACT', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### tan


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def tan(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, operation='TANGENT', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
### vector_curves


- node : [VectorCurves](/docs/Shader/VectorCurves.md)
- self : vector
- jump : vector
- return : self

##### Arguments

- fac : None
- mapping : None
- node_label : None
- node_color : None

#### Source code

``` python
def vector_curves(self, fac=None, mapping=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorCurves(fac=fac, vector=self, mapping=mapping, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.vector)
    return self
```
### wrap


- node : [VectorMath](/docs/Shader/VectorMath.md)
- self : vector
- jump : No
- return : output_socket

##### Arguments

- vector : None
- vector_1 : None
- node_label : None
- node_color : None

#### Source code

``` python
def wrap(self, vector=None, vector_1=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VectorMath(vector=self, vector_1=vector, vector_2=vector_1, operation='WRAP', node_label=node_label, node_color=node_color, **kwargs)
    return node.output_socket
```
