;; Extra Scheme Questions ;;

; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  (cond ((zero? a) b)
        ((zero? b) a)
        (else (gcd (min a b) (modulo (max a b) (min a b)))))
)


;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q9

; 定义一个函数，接受两个链表，然后返回第一个链表和第二个链表的差
; 注意：如果只有一个数或符号，不能将它括号括起来
(define (remove-from list1 list2)
  (if (null? list2) list1
      (remove-from (remove (car list2) list1) (cdr list2))
      )
  )

(define (split-aid lst n)
  (if (= 1 n) (cdr lst)
      (split-aid (cdr lst) (- n 1)))
      
  )
(define (split-at lst n)
  (cons (remove-from lst (split-aid lst n)) (split-aid lst n))
)
