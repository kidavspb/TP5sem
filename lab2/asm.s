	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 12, 0	sdk_version 12, 3
	.globl	_LFSR_Fibonacci                 ; -- Begin function LFSR_Fibonacci
	.p2align	2
_LFSR_Fibonacci:                        ; @LFSR_Fibonacci
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #16
	.cfi_def_cfa_offset 16
	str	x0, [sp, #8]
	ldr	x8, [sp, #8]
	ldr	w9, [x8]
	ldr	x8, [sp, #8]
	ldr	w8, [x8]
	eor	w8, w8, w9, lsr #1
	and	w9, w8, #0x1
	ldr	x8, [sp, #8]
	ldr	w8, [x8]
	lsr	w8, w8, #1
	orr	w8, w8, w9, lsl #3
	ldr	x9, [sp, #8]
	str	w8, [x9]
	ldr	x8, [sp, #8]
	ldr	w8, [x8]
	and	w0, w8, #0x1
	add	sp, sp, #16
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_my_enc                         ; -- Begin function my_enc
	.p2align	2
_my_enc:                                ; @my_enc
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #96
	stp	x29, x30, [sp, #80]             ; 16-byte Folded Spill
	add	x29, sp, #80
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	x0, [x29, #-8]
	stur	w1, [x29, #-12]
	stur	x2, [x29, #-24]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	ldur	x0, [x29, #-24]
	mov	x1, #1
	bl	_calloc
	stur	x0, [x29, #-32]
	stur	wzr, [x29, #-36]
	b	LBB1_1
LBB1_1:                                 ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB1_3 Depth 2
	ldursw	x8, [x29, #-36]
	ldur	x9, [x29, #-24]
	subs	x8, x8, x9
	b.hs	LBB1_8
	b	LBB1_2
LBB1_2:                                 ;   in Loop: Header=BB1_1 Depth=1
	str	wzr, [sp, #40]
	mov	w8, #7
	str	w8, [sp, #36]
	b	LBB1_3
LBB1_3:                                 ;   Parent Loop BB1_1 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	ldr	w8, [sp, #36]
	tbnz	w8, #31, LBB1_6
	b	LBB1_4
LBB1_4:                                 ;   in Loop: Header=BB1_3 Depth=2
	sub	x0, x29, #12
	bl	_LFSR_Fibonacci
	and	w8, w0, #0x1
	str	w8, [sp, #32]
	ldr	w9, [sp, #40]
	ldr	w8, [sp, #32]
	ldur	x10, [x29, #-8]
	ldursw	x11, [x29, #-36]
	ldrsb	w10, [x10, x11]
	ldr	w11, [sp, #36]
	asr	w10, w10, w11
	and	w10, w10, #0x1
	eor	w8, w8, w10
	orr	w8, w8, w9, lsl #1
	str	w8, [sp, #40]
	ldr	w8, [sp, #40]
                                        ; implicit-def: $x12
	mov	x12, x8
	ldr	w8, [sp, #32]
                                        ; implicit-def: $x10
	mov	x10, x8
	ldur	x8, [x29, #-8]
	ldursw	x9, [x29, #-36]
	ldrsb	w11, [x8, x9]
	ldr	w9, [sp, #36]
                                        ; implicit-def: $x8
	mov	x8, x9
	mov	x9, sp
	str	x12, [x9]
	str	x10, [x9, #8]
                                        ; implicit-def: $x10
	mov	x10, x11
	str	x10, [x9, #16]
	str	x8, [x9, #24]
	adrp	x0, l_.str.1@PAGE
	add	x0, x0, l_.str.1@PAGEOFF
	bl	_printf
	b	LBB1_5
LBB1_5:                                 ;   in Loop: Header=BB1_3 Depth=2
	ldr	w8, [sp, #36]
	subs	w8, w8, #1
	str	w8, [sp, #36]
	b	LBB1_3
LBB1_6:                                 ;   in Loop: Header=BB1_1 Depth=1
	ldr	w8, [sp, #40]
	ldur	x9, [x29, #-32]
	ldursw	x10, [x29, #-36]
	strb	w8, [x9, x10]
	ldur	x8, [x29, #-8]
	ldursw	x9, [x29, #-36]
	ldrsb	w13, [x8, x9]
	ldur	x8, [x29, #-8]
	ldursw	x9, [x29, #-36]
	ldrsb	w12, [x8, x9]
	ldur	x8, [x29, #-32]
	ldursw	x9, [x29, #-36]
	ldrb	w11, [x8, x9]
	ldur	x8, [x29, #-32]
	ldursw	x9, [x29, #-36]
	ldrb	w10, [x8, x9]
	mov	x9, sp
                                        ; implicit-def: $x8
	mov	x8, x13
	str	x8, [x9]
                                        ; implicit-def: $x8
	mov	x8, x12
	str	x8, [x9, #8]
                                        ; implicit-def: $x8
	mov	x8, x11
	str	x8, [x9, #16]
                                        ; implicit-def: $x8
	mov	x8, x10
	str	x8, [x9, #24]
	adrp	x0, l_.str.2@PAGE
	add	x0, x0, l_.str.2@PAGEOFF
	bl	_printf
	b	LBB1_7
LBB1_7:                                 ;   in Loop: Header=BB1_1 Depth=1
	ldur	w8, [x29, #-36]
	add	w8, w8, #1
	stur	w8, [x29, #-36]
	b	LBB1_1
LBB1_8:
	ldur	x8, [x29, #-32]
	ldur	x9, [x29, #-24]
	add	x8, x8, x9
	strb	wzr, [x8]
	ldur	x10, [x29, #-8]
	ldur	x8, [x29, #-32]
	mov	x9, sp
	str	x10, [x9]
	str	x8, [x9, #8]
	adrp	x0, l_.str.3@PAGE
	add	x0, x0, l_.str.3@PAGEOFF
	bl	_printf
	ldur	x0, [x29, #-32]
	ldp	x29, x30, [sp, #80]             ; 16-byte Folded Reload
	add	sp, sp, #96
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_my_dec                         ; -- Begin function my_dec
	.p2align	2
_my_dec:                                ; @my_dec
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #96
	stp	x29, x30, [sp, #80]             ; 16-byte Folded Spill
	add	x29, sp, #80
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	x0, [x29, #-8]
	stur	w1, [x29, #-12]
	stur	x2, [x29, #-24]
	adrp	x0, l_.str.4@PAGE
	add	x0, x0, l_.str.4@PAGEOFF
	bl	_printf
	ldur	x0, [x29, #-24]
	mov	x1, #1
	bl	_calloc
	stur	x0, [x29, #-32]
	stur	wzr, [x29, #-36]
	b	LBB2_1
LBB2_1:                                 ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB2_3 Depth 2
	ldursw	x8, [x29, #-36]
	ldur	x9, [x29, #-24]
	subs	x8, x8, x9
	b.hs	LBB2_8
	b	LBB2_2
LBB2_2:                                 ;   in Loop: Header=BB2_1 Depth=1
	str	wzr, [sp, #40]
	mov	w8, #7
	str	w8, [sp, #36]
	b	LBB2_3
LBB2_3:                                 ;   Parent Loop BB2_1 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	ldr	w8, [sp, #36]
	tbnz	w8, #31, LBB2_6
	b	LBB2_4
LBB2_4:                                 ;   in Loop: Header=BB2_3 Depth=2
	sub	x0, x29, #12
	bl	_LFSR_Fibonacci
	and	w8, w0, #0x1
	str	w8, [sp, #32]
	ldr	w9, [sp, #40]
	ldr	w8, [sp, #32]
	ldur	x10, [x29, #-8]
	ldursw	x11, [x29, #-36]
	ldrb	w10, [x10, x11]
	ldr	w11, [sp, #36]
	asr	w10, w10, w11
	and	w10, w10, #0x1
	eor	w8, w8, w10
	orr	w8, w8, w9, lsl #1
	str	w8, [sp, #40]
	ldr	w8, [sp, #40]
                                        ; implicit-def: $x12
	mov	x12, x8
	ldr	w8, [sp, #32]
                                        ; implicit-def: $x10
	mov	x10, x8
	ldur	x8, [x29, #-8]
	ldursw	x9, [x29, #-36]
	ldrb	w11, [x8, x9]
	ldr	w9, [sp, #36]
                                        ; implicit-def: $x8
	mov	x8, x9
	mov	x9, sp
	str	x12, [x9]
	str	x10, [x9, #8]
                                        ; implicit-def: $x10
	mov	x10, x11
	str	x10, [x9, #16]
	str	x8, [x9, #24]
	adrp	x0, l_.str.1@PAGE
	add	x0, x0, l_.str.1@PAGEOFF
	bl	_printf
	b	LBB2_5
LBB2_5:                                 ;   in Loop: Header=BB2_3 Depth=2
	ldr	w8, [sp, #36]
	subs	w8, w8, #1
	str	w8, [sp, #36]
	b	LBB2_3
LBB2_6:                                 ;   in Loop: Header=BB2_1 Depth=1
	ldr	w8, [sp, #40]
	ldur	x9, [x29, #-32]
	ldursw	x10, [x29, #-36]
	strb	w8, [x9, x10]
	ldur	x8, [x29, #-8]
	ldursw	x9, [x29, #-36]
	ldrb	w13, [x8, x9]
	ldur	x8, [x29, #-8]
	ldursw	x9, [x29, #-36]
	ldrb	w12, [x8, x9]
	ldur	x8, [x29, #-32]
	ldursw	x9, [x29, #-36]
	ldrb	w11, [x8, x9]
	ldur	x8, [x29, #-32]
	ldursw	x9, [x29, #-36]
	ldrb	w10, [x8, x9]
	mov	x9, sp
                                        ; implicit-def: $x8
	mov	x8, x13
	str	x8, [x9]
                                        ; implicit-def: $x8
	mov	x8, x12
	str	x8, [x9, #8]
                                        ; implicit-def: $x8
	mov	x8, x11
	str	x8, [x9, #16]
                                        ; implicit-def: $x8
	mov	x8, x10
	str	x8, [x9, #24]
	adrp	x0, l_.str.2@PAGE
	add	x0, x0, l_.str.2@PAGEOFF
	bl	_printf
	b	LBB2_7
LBB2_7:                                 ;   in Loop: Header=BB2_1 Depth=1
	ldur	w8, [x29, #-36]
	add	w8, w8, #1
	stur	w8, [x29, #-36]
	b	LBB2_1
LBB2_8:
	ldur	x8, [x29, #-32]
	ldur	x9, [x29, #-24]
	add	x8, x8, x9
	strb	wzr, [x8]
	ldur	x10, [x29, #-8]
	ldur	x8, [x29, #-32]
	mov	x9, sp
	str	x10, [x9]
	str	x8, [x9, #8]
	adrp	x0, l_.str.3@PAGE
	add	x0, x0, l_.str.3@PAGEOFF
	bl	_printf
	ldur	x0, [x29, #-32]
	ldp	x29, x30, [sp, #80]             ; 16-byte Folded Reload
	add	sp, sp, #96
	ret
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__cstring,cstring_literals
l_.str:                                 ; @.str
	.asciz	"-----\320\250\320\270\321\204\321\200\321\203\320\265\320\274-----\n"

l_.str.1:                               ; @.str.1
	.asciz	"%x = %x ^ (%x >> %d) & 0x01)\n"

l_.str.2:                               ; @.str.2
	.asciz	"%x (%c) -> %x (%c)\n"

l_.str.3:                               ; @.str.3
	.asciz	"%s -> %s\n\n\n"

l_.str.4:                               ; @.str.4
	.asciz	"-----\320\240\320\260\321\201\321\210\320\270\321\204\321\200\320\276\320\262\321\213\320\262\320\260\320\265\320\274-----\n"

.subsections_via_symbols
