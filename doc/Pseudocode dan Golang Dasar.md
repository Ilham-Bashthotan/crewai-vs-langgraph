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

## 1-output

Mencetak pada piranti keluaran (layar) dapat menggunakan perintah output, print, atau write. Dalam buku ini akan digunakan kata output secara konsisten. Contoh perintah output dapat dilihat pada Program 1-8. Sementara pada Golang, dapat mengunakan Println, Print, atau Printf dengan didahului nama library-nya, yaitu fmt.

### Program 1. Mencetak string "Hello, World!

``` pseudocode
program HelloWorld
kamus
    { tidak ada kamus }
algoritma
    output("Hello, World!")
endprogram
```

``` go
package main
import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

**Output:**
``` plaintext
Hello, World!
```

### Program 2. Mencetak string "Hello, World!"

``` pseudocode
program HelloWorld
kamus
    { tidak ada kamus }
algoritma
    output("Hello, World!")
endprogram
```

``` go
package main
import "fmt"

func main() {
    fmt.Print("Hello, World!")
}
```

**Output:**
``` plaintext
Hello, World!
```

### Program 3. Mencetak string "Hello, World!"

``` pseudocode
program HelloWorld
kamus
    { tidak ada kamus }
algoritma
    output("Hello, World!")
endprogram
```

``` go
package main
import "fmt"

func main() {
    fmt.Printf("%s\n", "Hello, World!")
}
```

**Output:**
``` plaintext
Hello, World!
```

### Program 4. Mencetak string "Hello, World!"

``` pseudocode
program HelloWorld
kamus
    { tidak ada kamus }
algoritma
    output("Hello, World!")
endprogram
```

``` go
package main
import "fmt"

func main() {
    fmt.Printf("Hello, World!")
}
```

**Output:**
``` plaintext
Hello, World!
```

### Program 5. Mencetak string "Hello, World!"

``` pseudocode
program HelloWorld
kamus
    a: string
algoritma
    a <- "Hello, World!"
    output(a)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a string
    a = "Hello, World!"
    fmt.Println(a)
}
```

**Output:**
``` plaintext
Hello, World!
```

### Program 6. Mencetak bilangan bulat

``` pseudocode
program BilanganBulat
kamus
    { tidak ada kamus }
algoritma
    output(1)
endprogram
```

``` go
ackage main
import "fmt"
func main() {
    fmt.Println(1)
}
```

**Output:**
``` plaintext
1
```

Untuk mencetak karakter, kita harus menggunakan Printf dengan format string %c seperti ditunjukkan pada Program 8.

### Program 8. Mencetak bilangan real

``` pseudocode
program BilanganBulat
kamus
    { tidak ada kamus }
algoritma
    output('a')
endprogram
```

``` go
ackage main
import "fmt"
func main() {
    fmt.Printf("%c\n", 'A')
}
```

**Output:**
``` plaintext
A
```

## 2-variabel-dan-tipe-data

Saat mendeklarasikan variabel perlu dituliskan pula tipe data yang dapat ditampung oleh variabel itu. Tipe data dasar (primitif) yang dikenal dalam bahasa pemrograman adalah numerik (bilangan bulat dan real), huruf (string dan karakter) serta boolean. Cara mendeklarasikannya dapat dilihat pada Program 9-16, yaitu dengan memberi tanda titik dua (:) di antara nama variabel dengan tipe datanya.

Dalam pemrograman kita tidak boleh mendeklarasikan identifier, termasuk nama variabel, dengan menggunakan keyword yang tersedia pada compiler. Berikut keyword dalam Golang yang tidak bisa dijadikan nama (identifier): import, type, const, var, func, package, map, chan, struct, interface, if, else, for, range, break, continue, goto, return, switch, case, select, default, fallthrough, defer, go.

Dalam pseudocode bilangan bulat dinyatakan dengan integer. Sementara dalam Golang terdapat banyak jenis tipe untuk integer ini, yaitu uint8, uint16, unit32, unit64, int8, int16, int32, int64. Umumnya digunakan int yang merupakan nama alias untuk int32 untuk komputer dengan sistem 32 bit dan int64 untuk komputer dengan sistem 64 bit.

### Program 9. Membuat variabel dengan tipe data bilangan bulat (integer)

``` pseudocode
program BilanganBulat
kamus
    bilangan : integer
algoritma
    bilangan <- 4
    output(bilangan)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var bilangan int
    bilangan = 4
    fmt.Println(bilangan)
}
```

**Output:**
``` plaintext
4
```

### Program 10. Membuat variabel dengan tipe data bilangan real

``` pseudocode
program BilanganReal
kamus
    bilangan : real
algoritma
    bilangan <- 2.5
    output(bilangan)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var bilangan float64
    bilangan = 2.5
    fmt.Println(bilangan)
}
```

**Output:**
``` plaintext
2.5
```
String dapat berupa huruf, bilangan, atau karakter khusus. Keyword yang digunakan untuk deklarasi string adalah string (Program 11).

### Program 11. Membuat variabel dengan tipe data string

``` pseudocode
program CetakString
kamus
    nama : string
algoritma
    nama <- "John Lennon"
    output(nama)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var nama string
    nama = "John Lennon"
    fmt.Println(nama)
}
```

**Output:**
``` plaintext
John Lennon
```

Untuk karakter digunakan tipe byte atau rune. Byte adalah tipe data untuk karakter ASCII, sedangkan rune untuk UTF-8. Byte sebetulnya adalah nama alias untuk uint8, sedangkan rune adalah nama alias untuk int32 (Program 12-13).

### Program 12. Membuat variabel dengan tipe data karakter

``` pseudocode
program CetakKarakter
kamus
    nilai : char
algoritma
    nilai <- 'A'
    output(nilai)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var nilai byte
    nilai = 'A'
    fmt.Printf("%c\n", nilai)
}
```

**Output:**
``` plaintext
A
```

### Program 13. Membuat variabel dengan tipe data karakter

``` pseudocode
program CetakKarakter
kamus
    nilai : char
algoritma
    nilai <- 'A'
    output(nilai)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var nilai rune
    nilai = 'A'
    fmt.Printf("%c\n", nilai)
}
```

**Output:**
``` plaintext
A
```

Variabel bertipe boolean pada Golang menggunakan keyword bool (Program 14).

### Program 14. Membuat variabel dengan tipe data boolean

``` pseudocode
program CetakBoolean
kamus
    ketemu : boolean
algoritma
    ketemu <- false
    output(ketemu)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var ketemu bool
    ketemu = false
    fmt.Println(ketemu)
}
```

**Output:**
``` plaintext
false
```

### Program 15. Membuat variabel dengan tipe data boolean

``` pseudocode
program CetakBoolean
kamus
    ketemu : boolean
algoritma
    ketemu <- true
    output(ketemu)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var ketemu bool
    ketemu = true
    fmt.Println(ketemu)
}
```

**Output:**
``` plaintext
true
```

### Program 16. Membuat variabel-variabel dengan tipe data bilangan bulat

``` pseudocode
program CetakBilanganBulat
kamus
    a, b : integer
algoritma
    a <- 1
    b <- 2
    output("Nilai a = ", a, "b = ", b)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b int
    a = 1
    b = 2
    fmt.Println("Nilai a =", a, "b =", b)
}
```

**Output:**
``` plaintext
Nilai a = 1 b = 2
```

## 3-konstanta

Deklarasi konstanta pada pseudocode ditulis menggunakan keyword constant, sedangkan pada Golang menggunakan const, setelah itu diikuti nama konstantanya tipe datanya serta nilainya (Program 17-18).

### Program 17. Membuat konstanta dengan tipe data bilangan real

``` pseudocode
program BuatKonstanta
kamus
    constant pi : real = 3.14
    radius : real
algoritma
    radius <- 10
    output(2 * pi * radius)
endprogram
```

``` go
package main
import "fmt"
func main() {
    const pi float64 = 3.14
    var radius float64
    radius = 10
    fmt.Println(2 * pi * radius)
}
```

**Output:**
``` plaintext
62.800000000000004
```

### Program 18. Membuat konstanta dengan tipe data bilangan bulat

``` pseudocode
program BuatKonstanta
kamus
    constant MAXTINGGI : integer = 170
    tinggi : integer
algoritma
    tinggi <- 165
    output(MAXTINGGI - tinggi)
endprogram
```

``` go
package main
import "fmt"
func main() {
    const MAXTINGGI int = 170
    var tinggi int
    tinggi = 165
    fmt.Println(MAXTINGGI - tinggi)
}
```

**Output:**
``` plaintext
5
```

## 4-komentar

Komentar pada pseudocode menggunakan awal dan akhir berupa kurawal. Sedangkan pada Golang menggunakan garis miring ganda (//) untuk komentar satu baris atau /* */ untuk komentar lebih dari satu baris.

### Program 19. Membuat komentar 1 baris
``` pseudocode
program Komentar
kamus
    a : integer
algoritma
    input(a) {membaca data}
    output(a) {mencetak data}
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a int
    fmt.Scan(&a) // membaca data
    fmt.Println(a) // mencetak data
}
```

**Input:**
``` plaintext
5
```

**Output:**
``` plaintext
5
```

### Program 20. Membuat komentar lebih dari 1 baris

``` pseudocode
program Komentar
    { program ini akan membaca masukan
    berupa bilangan bulat dan mencetaknya
    di layar}
kamus
    a : integer
algoritma
    input(a)
    output(a)
endprogram
```

``` go
package main
import "fmt"
func main() {
    /* program ini akan membaca masukan
    berupa bilangan bulat dan mencetak di
    layar */
    var a int
    fmt.Scan(&a)
    fmt.Println(a)
}
```

**Input:**
``` plaintext
5
```

**Output:**
``` plaintext
5
```

## 5-input-dan-output

Perintah membaca (input atau masukan) dari piranti masukan dapat menggunakan read atau input. Dalam buku ini secara konsisten digunakan input, sedangkan dalam Golang digunakan Scan, Scanln, atau Scanf dengan didahului fmt.

### Program 21. Membuat input dan output bilangan bulat

``` pseudocode
program IO
kamus
    a : integer
algoritma
    input(a)
    output(a)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a int
    fmt.Scan(&a)
    fmt.Println(a)
}
```

**Input:**
``` plaintext
5
```

**Output:**
``` plaintext
5
```

### Program 22. Membuat input dan output bilangan real

``` pseudocode
program IO
kamus
    a : real
algoritma
    input(a)
    output(a)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a float64
    fmt.Scan(&a)
    fmt.Println(a)
}
```

**Input:**
``` plaintext
5.5
```

**Output:**
``` plaintext
5.5
```

### Program 23. Membuat input dan output string

``` pseudocode
program IO
kamus
    a : string
algoritma
    input(a)
    output(a)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a string
    fmt.Scan(&a)
    fmt.Println(a)
}
```

**Input:**
``` plaintext
Telkom
```

**Output:**
``` plaintext
Telkom
```
Input string tidak akan dibaca lengkap jika terdapat spasi pada datanya. "Telkom University" hanya akan terbaca "Telkom" (Program 24).

### Program 24. Membuat input dan output string

``` pseudocode
program IO
kamus
    a : string
algoritma
    input(a)
    output(a)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a string
    fmt.Scan(&a)
    fmt.Println(a)
}
```

**Input:**
``` plaintext
Telkom University
```

**Output:**
``` plaintext
Telkom
```
Untuk membaca masukan karakter gunakan Scanf seperti ditunjukkan pada Program 25.

### Program 25. Membuat input dan output karakter

``` pseudocode
program IO
kamus
    a, b : char
algoritma
    input(a, b)
    output(a b,)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b byte
    fmt.Scanf("%c%c", &a, &b)
    fmt.Printf("%c %c\n", a, b)
}
```

**Input:**
``` plaintext
qw
```

**Output:**
``` plaintext
q w
```

### Program 26. Membuat input dan output boolean

``` pseudocode
program IO
kamus
    a, b : boolean
algoritma
    input(a, b)
    output(b, a)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b bool
    fmt.Scan(&a, &b)
    fmt.Print(b, a)
}
```

**Input:**
``` plaintext
true false
```

**Output:**
``` plaintext
false true
```

## 6-operator

Operator assignment atau penugasan pada pseudocode menggunakan tanda panah ke arah kiri (<-). Sementara itu pada Golang digunakan tanda sama dengan
(=).

### Program 27. Membuat assignment
``` pseudocode
program Operator
kamus
    a, b, c : integer
algoritma
    input(a, b)
    c <- a + b
    output(c)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b, c int
    fmt.Scan(&a, &b)
    c = a + b
    fmt.Println(c)
}
```

**Input:**
``` plaintext
1 2
```

**Output:**
``` plaintext
3
```

Operator aritmatika terdiri atas penjumlahan (+), pengurangan (-), perkalian (*),
pembagian (/), modulo (mod).

### Program 28. Membuat operasi aritmatika penjumlahan

``` pseudocode
program Operator
kamus
    a, b : integer
algoritma
    input(a, b)
    output(a + b)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b int
    fmt.Scan(&a, &b)
    fmt.Println(a + b)
}
```

**Input:**
``` plaintext
1 2
```

**Output:**
``` plaintext
3
```

### Program 29. Membuat operasi aritmatika pengurangan

``` pseudocode
program Operator
kamus
    a, b : in   teger
algoritma
    input(a, b)
    output(a - b)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b int
    fmt.Scan(&a, &b)
    fmt.Println(a - b)
}
```

**Input:**
``` plaintext
1 2
```

**Output:**
``` plaintext
-1
```

### Program 30. Membuat operasi aritmatika perkalian

``` pseudocode
program Operator
kamus
    a, b : integer
algoritma
    input(a, b)
    output(a * b)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b int
    fmt.Scan(&a, &b)
    fmt.Println(a * b)
}
```

**Input:**
``` plaintext
1 2
```

**Output:**
``` plaintext
2
```

Pembagian bilangan bulat (integer division) pada pseudocode menggunakan keyword div, sedangkan pada Golang menggunakan tanda /. Perhatikan perbedaan antara pembagian bilangan real (Program 31) dengan bilangan bulat (Program 32).

### Program 31. Membuat operasi aritmatika pembagian bilangan real

``` pseudocode
program Operator
kamus
    a, b : real
algoritma
    input(a, b)
    output(a / b)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b float64
    fmt.Scan(&a, &b)
    fmt.Println(a / b)
}
```

**Input:**
``` plaintext
1 2
```

**Output:**
``` plaintext
0.5
```

### Program 32. Membuat operasi aritmatika pembagian bilangan bulat (integer

``` pseudocode
division)
program Operator
kamus
    a, b : integer
algoritma
    input(a, b)
    output(a div b)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b int
    fmt.Scan(&a, &b)
    fmt.Println(a / b)
}
```

**Input:**
``` plaintext
1 2
```

**Output:**
``` plaintext
0
```
Sisa dari pembagian menggunakan keyword mod, sedangklan pada Golang menggunakan tanda %.

### Program 33. Membuat operasi aritmatika pembagian modulo

``` pseudocode
program Operator
kamus
    a, b : integer
algoritma
    input(a, b)
    output(a mod b)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b int
    fmt.Scan(&a, &b)
    fmt.Println(a % b)
}
```

**Input:**
``` plaintext
1 2
```

**Output:**
``` plaintext
2
```

Operasi perbandingan atau relasi menggunakan operator relasi <, <=, >, >=, ==, dan !=.

### Program 34. Membuat operasi perbandingan lebih kecil dari

``` pseudocode
program Operator
kamus
    a, b : integer
algoritma
    input(a, b)
    output(a < b)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b int
    fmt.Scan(&a, &b)
    fmt.Println(a < b)
}
```

**Input:**
``` plaintext
1 2
```

**Output:**
``` plaintext
true
```

### Program 35. Membuat operasi perbandingan lebih kecil dari atau sama dengan

``` pseudocode
program Operator
kamus
    a, b : integer
algoritma
    input(a, b)
    output(a <= b)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b int
    fmt.Scan(&a, &b)
    fmt.Println(a <= b)
}
```

**Input:**
``` plaintext
1 2
```

**Output:**
``` plaintext
true
```

### Program 36. Membuat operasi perbandingan lebih besar dari

``` pseudocode
program Operator
kamus
    a, b : integer
algoritma
    input(a, b)
    output(a > b)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b int
    fmt.Scan(&a, &b)
    fmt.Println(a > b)
}
```

**Input:**
``` plaintext
1 2
```

**Output:**
``` plaintext
false
```

### Program 37. Membuat operasi perbandingan lebih besar dari atau sama dengan

``` pseudocode
program Operator
kamus
    a, b : integer
algoritma
    input(a, b)
    output(a >= b)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b int
    fmt.Scan(&a, &b)
    fmt.Println(a >= b)
}
```

**Input:**
``` plaintext
1 2
```

**Output:**
``` plaintext
false
```

### Program 38. Membuat operasi perbandingan sama dengan

``` pseudocode
program Operator
kamus
    a, b : integer
algoritma
    input(a, b)
    output(a == b)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b int
    fmt.Scan(&a, &b)
    fmt.Println(a == b)
}
```

**Input:**
``` plaintext
1 2
```

**Output:**
``` plaintext
false
```
<-
### Program 39. Membuat operasi perbandingan tidak sama dengan

``` pseudocode
program Operator
kamus
    a, b : integer
algoritma
    input(a, b)
    output(a != b)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b int
    fmt.Scan(&a, &b)
    fmt.Println(a == b)
}
```

**Input:**
``` plaintext
1 2
```

**Output:**
``` plaintext
true
```
Operator logika pada pseudocode menggunakan keyword and, or, dan not, sedangkan pada Golang menggunakan &&, ||, dan !.

### Program 40. Membuat operasi logika AND

``` pseudocode
program Operator
kamus
    a, b : boolean
algoritma
    input(a, b)
    output(a and b)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b bool
    fmt.Scan(&a, &b)
    fmt.Println(a && b)
}
```

**Input:**
``` plaintext
true true
```

**Output:**
``` plaintext
true
```

### Program 41. Membuat operasi logika OR

``` pseudocode
program Operator
kamus
    a, b : boolean
algoritma
    input(a, b)
    output(a or b)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b bool
    fmt.Scan(&a, &b)
    fmt.Println(a || b)
}
```

**Input:**
``` plaintext
true true
```

**Output:**
``` plaintext
true
```

### Program 42. Membuat operasi logika NOT

``` pseudocode
program Operator
kamus
    a : boolean
algoritma
    input(a)
    output(not a)
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a bool
    fmt.Scan(&a)
    fmt.Println(!a)
}
```

**Input:**
``` plaintext
true
```

**Output:**
``` plaintext
false
```



## 7-perulangan

Perulangan for-to-do pada pseudocode secara implisit sudah mendapat incriment 1 (Program 43). Sementara pada Golang, secara eksplisit dituliskan incriment-nya.

### Program 43. Membuat perulangan for-to-do

``` pseudocode
program Perulangan
kamus
    a, b, i : integer
algoritma
    input(a, b)
    for i <- a to b do
		output(i)
    endfor
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b, i int
    fmt.Scan(&a, &b)
    for i = a; i <= b; i++ {
        fmt.Println(i)
    }
}
```

**Input:**
``` plaintext
1 3
```

**Output:**
``` plaintext
1
2
3
```

Perulangan for-down-to secara implisit sudah mendapat decrement sebesar 1 (Program 44). Sementara pada Golang secara eksplisit dituliskan decrement-nya.

### Program 44. Membuat perulangan for-down-to

``` pseudocode
program Perulangan
kamus
    a, b, i : integer
algoritma
    input(a, b)
    for i <- a downto b do
		output(i)
    endfor
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b, i int
    fmt.Scan(&a, &b)
    for i = a; i >= b; i-- {
        fmt.Println(i)
    }
}
```

**Input:**
``` plaintext
3 1
```

**Output:**
``` plaintext
3
2
1
```
Pada pseudocode while-do menggunakan sintaks seperti ditunjukkan padaSementara itu pada Golang, tidak ada keyword while. Sebagai gantinya digunakan keyword for.

### Program 45. Membuat perulangan while-do

``` pseudocode
program Perulangan
kamus
    a, b, i : integer
algoritma
    input(a, b)
    i <- a
    while i <= b do
		output(i)
		      i <- i + 1
    endwhile
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b, i int
    fmt.Scan(&a, &b)
    i = a
    for i <= b {
        fmt.Println(i)
        i++
    }
}
```

**Input:**
``` plaintext
1 3
```

**Output:**
``` plaintext
1
2
3
```

Sintaks repeat-until pada pseudocode menggunakan perintah sebagaimana tampak pada Program 45. Sedangkan pada Golang menggunakan keyword for dengan beberapa versi penulisan (Program 46-47).

### Program 46. Membuat perulangan repeat-until (1)

``` pseudocode
program Perulangan
kamus
    a, b, i : integer
algoritma
    input(a, b)
    i <- a
    repeat
		output(i)
		      i <- i + 1
    until i > b
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b, i int
    fmt.Scan(&a, &b)
    i = a
    for {
        fmt.Println(i)
        i++
        if i > b {
            break
        }
    }
}
```

**Input:**
``` plaintext
1 0
```

**Output:**
``` plaintext
1
```

### Program 47. Membuat perulangan repeat-until (2)

``` pseudocode
program Perulangan
kamus
    a, b, i : integer
algoritma
    input(a, b)
    i <- a
    repeat
		output(i)
		i <- i + 1
    until i > 3
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a, b, i int
    var ok bool
    fmt.Scan(&a, &b)
    i = a
    for ok = true; ok; ok = !(i > b) {
        fmt.Println(i)
        i++
    }
}
```

**Input:**
``` plaintext
1 0
```

**Output:**
``` plaintext
1
```

### Program 48. Membuat perulangan repeat-until (3)

``` pseudocode
program Perulangan
kamus
    a, b, i : integer
algoritma
    input(a, b)
    i <- a
    repeat
		output(i)
    until i > 3
endprogram
```

``` go
package main
import "fmt"
func main() {
    var i, a, b int
    var selesai bool
    fmt.Scan(&a, &b)
    i <- i + 1
    i = a
    for selesai = false; !selesai; {
        fmt.Println(i)
        i++
        selesai = i > b
    }
}
```

**Input:**
``` plaintext
1 0
```

**Output:**
``` plaintext
1
```

Untuk perulangan bersarang (nested loop) kita bisa menggunakan sintaks seperti pada Program 49-50.

### Program 49. Membuat perulangan bersarang (nested loop).

``` pseudocode
program PerulanganBersarang
kamus
i, j : integer
algoritma
    for i <- 0 to 1 do
		output("Satu ")
		for j <- 0 to 1 do
			output("Dua ")
		endfor
    endfor
endprogram
```

``` go
package main
import "fmt"
func main() {
    var i, j int
    for i = 0; i < 2; i++ {
        fmt.Print("Satu ")
        for j = 0; j < 2; j++ {
            fmt.Print("Dua ")
        }
    }
}
```

**Output:**
``` plaintext
Satu Dua Dua Satu Dua Dua %
```

### Program 50. Membuat perulangan bersarang (nested loop).

``` pseudocode
program PerulanganBersarang
kamus
i, j : integer
algoritma
    i <- 0
    while i < 2 do
		output("Satu ")
		j <- 0
		while j < 2 do
			output("Dua ")
			j <- j + 1
		endwhile
		i <- i + 1
    endwhile
endprogram
```

``` go
package main
import "fmt"
func main() {
    var i, j int
    i = 0
    for i < 2 {
        fmt.Print("Satu ")
        j = 0
        for j < 2 {
            fmt.Print("Dua ")
            j++
        }
        i++
    }
}
```

**Output:**
``` plaintext
Satu Dua Dua Satu Dua Dua %
```

## 8-percabangan

Pernyataan if pada struktur percabangan menggunakan if - then seperti ditunjukkan pada Program 51.

### Program 51. Membuat percabangan if
``` pseudocode
program Percabangan
kamus
    a : integer
algoritma
    input(a)
    if a > 6 then
		output("Hello")
    endif
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a int
    fmt.Scan(&a)
    if a > 6 {
        fmt.Println("Hello")
    }
}
```

**Input:**
``` plaintext
9
```

**Output:**
``` plaintext
Hello
```
Pernyataan if dengan else menggunakan if - then - else seperti ditunjukkan pada
Program 52.

### Program 52. Membuat percabangan if-else
``` pseudocode
program Percabangan
kamus
    a : integer
algoritma
    input(a)
    if a > 6 then
		output("Hello")
    else
		output("Hi")
    endif
endprogram
```

``` go
package main
import "fmt"
    func main() {
    var a int
    fmt.Scan(&a)
    if a > 6 {
        fmt.Println("Hello")
    } else {
        fmt.Println("Hi")
    }
}
```

**Input:**
``` plaintext
3
```

**Output:**
``` plaintext
Hi
```
Pernyataan if dengan cabang else if menggunakan sintaks seperti ditunjukkan pada Program 53 dan 54.

### Program 53. Membuat percabangan if-else if
``` pseudocode
program Percabangan
kamus
a : integer
algoritma
    input(a)
    if a > 6 then
		output("Hello")
    else if a < 6 then
		output("Hi")
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a int
    fmt.Scan(&a)
    if a > 6 {
        fmt.Println("Hello")
    } else if a < 6 {
        fmt.Println("Hi")
    }
}
```

**Input:**
``` plaintext
3
```

**Output:**
``` plaintext
Hi
```

### Program 54. Membuat percabangan if-else if-else
``` pseudocode
program Percabangan
kamus
    a : integer
algoritma
    input(a)
    if a > 6 then
		output("Hello")
    else if a < 6 then
		output("Hi")
    else
		output("Yes")
    endif
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a int
    fmt.Scan(&a)
    if a > 6 {
        fmt.Println("Hello")
    } else if a < 6 {
        fmt.Println("Hi")
    } else {
        fmt.Println("Yes")
    }
}
```

**Input:**
``` plaintext
3
```

**Output:**
``` plaintext
Yes
```
Jika terdapat percabangan yang lebih dari 3, disarankan menggunakan sintaks switch-case sebagaimana terlihat pada Program 55 dan 56. Pada pseudocode digunakan keyword depend on, sedangkan pada Golang digunakan keyword switch case.

### Program 55. Membuat percabangan switch-case
``` pseudocode
program Percabangan
kamus
    a : integer
algoritma
    input(a)
    depend on (a)
        1 : output("Hello")
        2 : output("Hi")
        3 : output("Hola")
		default: output("No")
    enddependon
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a int
    fmt.Scan(&a)
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
}
```

**Input:**
``` plaintext
1
```

**Output:**
``` plaintext
Hello
```

### Program 56. Membuat percabangan switch-case
``` pseudocode
program Percabangan
kamus
    a : integer
algoritma
    input(a)
    depend on
        a == 1 : output("Hello")
        a == 2 : output("Hi")
        a == 3 : output("Hola")
		default: output("No")
    enddependon
endprogram
```

``` go
package main
import "fmt"
func main() {
    var a int
    fmt.Scan(&a)
    switch {
        case a == 1:
            fmt.Println("Hello")
        case a == 2:
            fmt.Println("Hi")
        case a == 3:
            fmt.Println("Hola")
        default:
            fmt.Println("No")
    }
}
```

**Input:**
``` plaintext
2
```

**Output:**
``` plaintext
Hi
```

### Program 57. Membuat percabangan bersarang (nested-if)
``` pseudocode
program Percabangan
kamus
    umur : integer
algoritma
    input(umur)
    if umur <= 18 then
		if umur <= 10 then
			output("anak-anak")
		else
			output("remaja")
	    endif
    else
		output("non remaja/anak-anak")
    endif
endprogram
```

``` go
package main
import "fmt"
func main() {
    var umur int
    fmt.Scan(&umur)
    if umur <= 18 {
        if umur <= 10 {
            fmt.Println("Anak-anak")
        } else {
            fmt.Println("Remaja")
        }
    } else {
        fmt.Println("Non remaja/Anak-anak")
    }
}
```

**Input:**
``` plaintext
5
```

**Output:**
``` plaintext
anak-anak
```



## 9-perulangan-dan-percabangan

Badan perulangan pada pernyataan perulangan dapat berisi perulangan lagi atau percabangan. Pada Program 57 dan 58 ditunjukkan contoh penulisan percabangan dalam badan perulangan.

### Program 58. Membuat perulangan dan percabangan
``` pseudocode
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

``` go
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

**Input:**
``` plaintext
1 5
```

**Output:**
``` plaintext
2
4
```