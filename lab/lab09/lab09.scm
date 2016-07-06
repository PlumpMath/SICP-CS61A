;; Scheme ;;

; Q1
(define (over-or-under x y)
  (cond ((= x y) 0)
        ((> x y) 1)
        ((< x y) -1)
  )
)


; Q3
(define lst
  (cons (cons 1 '())
        (cons 2
              (cons (cons 3 4)
                    (cons 5 '()))))
)
; Q4
(define (remove item lst)
   (cond ((null? lst) '())
         ((equal? (car lst) item) (remove item (cdr lst)))
         (else (cons (car lst) (remove item (cdr lst))))
    )
)
;;; Tests

(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q5
(define (filter f lst)
  (cond ((null? lst) '())
        ((f (car lst)) (cons (car lst) (filter f (cdr lst))))
        (else (filter f (cdr lst))))
)


;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter even? '(0 1 1 2 3 5 8))
; expect (0 2 8)

; Q6
(define (make-adder num)
  (lambda (x) (+ x num))
)
;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13

; Q7
(define (composed f g)
  (lambda (x) (f (g x)))
)
