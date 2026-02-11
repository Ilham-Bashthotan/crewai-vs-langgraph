# Pseudocode dan Golang Dasar

## Daftar Isi

1. [Output](#1-output)
2. [Variabel dan Tipe Data](#2-variabel-dan-tipe-data)
3. [Konstanta](#3-konstanta)
4. [Komentar](#4-komentar)
5. [Input dan Output](#5-input-dan-output)
6. [Operator](#6-operator)
7. [Perulangan](#7-perulangan)
8. [Percabangan](#8-percabangan)
9. [Perulangan dan Percabangan](#9-perulangan-dan-percabangan)

---

## Referensi Cepat: Pseudocode ke Golang

| Konsep | Pseudocode | Golang |
|---|---|---|
| Output | `output(x)` | `fmt.Println(x)` / `fmt.Printf(...)` |
| Input | `input(x)` | `fmt.Scan(&x)` / `fmt.Scanf(...)` |
| Assignment | `x <- nilai` | `x = nilai` |
| Komentar 1 baris | `{ komentar }` | `// komentar` |
| Komentar multiline | `{ baris1` `baris2 }` | `/* baris1` `baris2 */` |
| Bilangan bulat | `integer` | `int` |
| Bilangan real | `real` | `float64` |
| Karakter | `char` | `byte` / `rune` |
| Logika | `boolean` | `bool` |
| Konstanta | `constant x : tipe = nilai` | `const x tipe = nilai` |
| AND / OR / NOT | `and` / `or` / `not` | `&&` / `\|\|` / `!` |
| Pembagian bulat | `a div b` | `a / b` (tipe `int`) |
| Modulo | `a mod b` | `a % b` |

---

## 1. Output

Output ke layar menggunakan `output(...)`. Di Golang: `fmt.Println`, `fmt.Print`, atau `fmt.Printf`.

Cetak karakter wajib menggunakan `fmt.Printf` dengan format `%c`.

```pseudocode
output("Hello, World!")        { string }
output(1)                       { bilangan bulat }
output('A')                     { karakter }
output("Nilai a =", a, "b =", b){ beberapa nilai }
```

```go
fmt.Println("Hello, World!")
fmt.Println(1)
fmt.Printf("%c\n", 'A')
fmt.Println("Nilai a =", a, "b =", b)
```

---

## 2. Variabel dan Tipe Data

Deklarasi variabel: `nama : tipe`. Di Golang: `var nama tipe`.

Kata yang tidak boleh dijadikan nama variabel di Golang: `import`, `type`, `const`, `var`, `func`, `package`, `map`, `chan`, `struct`, `interface`, `if`, `else`, `for`, `range`, `break`, `continue`, `goto`, `return`, `switch`, `case`, `select`, `default`, `fallthrough`, `defer`, `go`.

```pseudocode
kamus
    bilangan : integer      { -> var bilangan int }
    nilai    : real         { -> var nilai float64 }
    nama     : string       { -> var nama string }
    karakter : char         { -> var karakter byte / rune }
    ketemu   : boolean      { -> var ketemu bool }
    a, b     : integer      { -> var a, b int }
```

Contoh penggunaan:

```pseudocode
program ContohVariabel
kamus
    a, b : integer
algoritma
    a <- 1
    b <- 2
    output("Nilai a =", a, "b =", b)
endprogram
```

```go
package main
import "fmt"
func main() {
    var a, b int
    a = 1
    b = 2
    fmt.Println("Nilai a =", a, "b =", b)
}
```

**Output:** `Nilai a = 1 b = 2`

---

## 3. Konstanta

```pseudocode
constant pi       : real    = 3.14
constant MAXTINGGI: integer = 170
```

```go
const pi        float64 = 3.14
const MAXTINGGI int     = 170
```

---

## 4. Komentar

```pseudocode
input(a)  {membaca data}

{ program ini akan membaca masukan
  berupa bilangan bulat dan mencetaknya }
```

```go
fmt.Scan(&a) // membaca data

/* program ini akan membaca masukan
   berupa bilangan bulat dan mencetaknya */
```

---

## 5. Input dan Output

```pseudocode
input(a)     { membaca satu nilai }
input(a, b)  { membaca dua nilai }
```

```go
fmt.Scan(&a)
fmt.Scan(&a, &b)
```

Catatan penting:
- `fmt.Scan` untuk `int`, `float64`, `bool`, `string` (berhenti di spasi).
- Input `string` dengan spasi hanya terbaca hingga spasi pertama.
- Input `char`: gunakan `fmt.Scanf("%c%c", &a, &b)`.
- Output `char`: gunakan `fmt.Printf("%c\n", a)`.

---

## 6. Operator

### Aritmatika

| Operasi | Pseudocode | Golang |
|---|---|---|
| Penjumlahan | `a + b` | `a + b` |
| Pengurangan | `a - b` | `a - b` |
| Perkalian | `a * b` | `a * b` |
| Pembagian real | `a / b` | `a / b` (tipe `float64`) |
| Pembagian bulat | `a div b` | `a / b` (tipe `int`) |
| Modulo | `a mod b` | `a % b` |

Pembagian `int` di Go otomatis integer division. Modulo `1 % 2` menghasilkan `1`.

### Perbandingan

`<`, `<=`, `>`, `>=`, `==`, `!=` — sama di pseudocode dan Golang.

### Logika

| Pseudocode | Golang |
|---|---|
| `a and b` | `a && b` |
| `a or b` | `a \|\| b` |
| `not a` | `!a` |

---

## 7. Perulangan

### for-to-do (increment 1)

```pseudocode
for i <- a to b do
    output(i)
endfor
```

```go
for i = a; i <= b; i++ {
    fmt.Println(i)
}
```

### for-downto (decrement 1)

```pseudocode
for i <- a downto b do
    output(i)
endfor
```

```go
for i = a; i >= b; i-- {
    fmt.Println(i)
}
```

### while-do

```pseudocode
i <- a
while i <= b do
    output(i)
    i <- i + 1
endwhile
```

```go
i = a
for i <= b {
    fmt.Println(i)
    i++
}
```

### repeat-until

Dieksekusi minimal 1 kali, berhenti saat kondisi `until` terpenuhi.

```pseudocode
i <- a
repeat
    output(i)
    i <- i + 1
until i > b
```

```go
i = a
for {
    fmt.Println(i)
    i++
    if i > b {
        break
    }
}
```

### Nested Loop

```pseudocode
for i <- 0 to 1 do
    output("Satu ")
    for j <- 0 to 1 do
        output("Dua ")
    endfor
endfor
```

```go
for i = 0; i < 2; i++ {
    fmt.Print("Satu ")
    for j = 0; j < 2; j++ {
        fmt.Print("Dua ")
    }
}
```

**Output:** `Satu Dua Dua Satu Dua Dua`

---

## 8. Percabangan

### if

```pseudocode
if kondisi then
    ...
endif
```

```go
if kondisi {
    ...
}
```

### if-else

```pseudocode
if kondisi then
    ...
else
    ...
endif
```

```go
if kondisi {
    ...
} else {
    ...
}
```

### if-else if-else

```pseudocode
if a > 6 then
    output("Hello")
else if a < 6 then
    output("Hi")
else
    output("Yes")
endif
```

```go
if a > 6 {
    fmt.Println("Hello")
} else if a < 6 {
    fmt.Println("Hi")
} else {
    fmt.Println("Yes")
}
```

### switch-case (depend on)

Gunakan saat cabang lebih dari 3.

```pseudocode
depend on (a)
    1 : output("Hello")
    2 : output("Hi")
    3 : output("Hola")
    default: output("No")
enddependon
```

```go
switch a {
case 1:
    fmt.Println("Hello")
case 2:
    fmt.Println("Hi")
case 3:
    fmt.Println("Hola")
default:
    fmt.Println("No")
}
```

Variasi tanpa ekspresi (`depend on` dengan kondisi eksplisit):

```pseudocode
depend on
    a == 1 : output("Hello")
    ...
enddependon
```

```go
switch {
case a == 1:
    fmt.Println("Hello")
...
}
```

### Nested if

```pseudocode
if umur <= 18 then
    if umur <= 10 then
        output("anak-anak")
    else
        output("remaja")
    endif
else
    output("non remaja/anak-anak")
endif
```

```go
if umur <= 18 {
    if umur <= 10 {
        fmt.Println("anak-anak")
    } else {
        fmt.Println("remaja")
    }
} else {
    fmt.Println("non remaja/anak-anak")
}
```

---

## 9. Perulangan dan Percabangan

Percabangan dapat ditempatkan di dalam badan perulangan.

```pseudocode
program PerulanganPercabangan
kamus
    a, b, i : integer
algoritma
    input(a, b)
    for i <- a to b do
        if i mod 2 == 0 then
            output(i)
        endif
    endfor
endprogram
```

```go
package main
import "fmt"
func main() {
    var a, b, i int
    fmt.Scan(&a, &b)
    for i = a; i <= b; i++ {
        if i%2 == 0 {
            fmt.Println(i)
        }
    }
}
```

**Input:** `1 5` | **Output:** `2` `4`