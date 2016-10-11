(define (cddr s)
  (cdr (cdr s)))
  
(define (cadr s)
   (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)


(define (square x) (* x x))
(define (div-two x) (/ x 2))
(define (div-two-one x) ( / (- x 1) 2))
(define (is-even x) 
    (= x (* (quotient x 2) 2)
        )
    )

(define (pow b n)
    (if (eq? n 0) 1
            (if (is-even n)
                    (square (pow b (div-two n)))
                    (* b (square (pow b (div-two-one n)))
                        )
                )
        )
)



(define (ordered? s)
    (if (eq? s nil) True
            (if (eq? (cdr s) nil) True
                    (if (> (car s) (cadr s)) False ;//first element bigger than second
                            (ordered? (cdr s))
                        )
                )
        )
)
(define (app x lister)
    (if (eq? lister nil) False
            (if (eq? x (car lister)) True
                    (app  x (cdr lister))
                ) 
        )
    )
(define (no-repeats s)
    (if (eq? s nil) s
            (if (app (car s) (cdr s)) (no-repeats (cdr s))
                    (cons (car s) (no-repeats (cdr s))
                )
        )
  )
)

(define (nodots s)
  'YOUR-CODE-HERE
  (if (not (pair? s))
      (if (null? s)
      s
      (cons s nil))
      (if (pair? (car s))
      (cons (nodots (car s)) (nodots (cdr s)))
      (cons (car s) (nodots (cdr s)))))
)

; Sets as sorted lists

(define (nq x y)
    (if (eq? x y) False True)
    )
 
(define (empty? s) (null? s))
(define (contains? s v)
    (cond ((empty? s) false)
          ((eq? (car s) v) True)
          ((nq (car s) v) (contains? (cdr s) v))
          (else nil) ; replace this line
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return len(s) == 0
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)
(define (add s v)
    (cond ((empty? s) (list v))
          ((< (car s) v) (cons (car s) (add (cdr s) v)))
          ((> (car s) v) (cons v s)) ; replace this line
          ((= (car s) v) s)

          )
    )

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          ((eq? (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
          ((< (car s) (car t)) (intersect (cdr s) t))
          ((> (car s) (car t)) (intersect s (cdr t))) 
          ))


; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ((eq? (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))))
          ((< (car s) (car t)) (cons (car s) (union (cdr s)  t)))
          ((> (car s) (car t)) (cons (car t) (union s (cdr t))))
          ))




; A data abstraction for binary trees where nil represents the empty tree
(define (tree label left right) (list label left right))
(define (label t) (car t))
(define (left t) (cadr t))
(define (right t) (caddr t))
(define (empty? s) (null? s))
(define (leaf label) (tree label nil nil))
(define (in? t v)
    (cond ((empty? t) false)
          'YOUR-CODE-HERE
          (else nil)
          ))

; Equivalent Python code, for your reference:
;
; def contains(s, v):
;     if s.is_empty:
;         return False
;     elif s.label == v:
;         return True
;     elif s.label < v:
;         return contains(s.right, v)
;     elif s.label > v:
;         return contains(s.left, v)

(define (as-list t)
    (cond ((empty? t) t)
      ((empty? (left t)) (cons (label t) (as-list (right t))))
      (else (cons-list (as-list (left t)) (cons (label t) (as-list (right t))))))
)
