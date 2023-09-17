open System

type BiSquareRootResult =
    | NoRoots
    | OneRoot of double
    | TwoRoots of double * double
    | ThreeRoots of double * double * double
    | FourRoots of double * double * double * double

let CalculateRoots(a: double, b: double, c: double): BiSquareRootResult =
    let D = b * b - 4.0 * a * c

    if a = 0 then
        let pre_rt = -c / b
        match pre_rt with
        |r when r < 0 -> NoRoots
        |r when r = 0 -> OneRoot 0.0 
        |r -> TwoRoots (Math.Sqrt(r), -Math.Sqrt(r))
    else if D < 0.0 then
        NoRoots
    else if D = 0.0 then
        let pre_rt = -b / (2.0 * a)
        match pre_rt with
        |r when r < 0 -> NoRoots
        |r when r = 0 -> OneRoot 0.0 
        |r -> TwoRoots (Math.Sqrt(r), -Math.Sqrt(r))
    else
        let sqrtD = Math.Sqrt(D)
        let pre_rt1 = (-b + sqrtD) / (2.0 * a)
        let pre_rt2 = (-b - sqrtD) / (2.0 * a)

        match pre_rt1, pre_rt2 with
        |r1, r2 when r1 = 0.0 && r2 < 0.0 -> OneRoot 0.0
        |r1, r2 when r1 < 0.0 && r2 = 0.0 -> OneRoot 0.0
        |r1, r2 when r1 < 0.0 && r2 < 0.0 -> NoRoots
        |r1, r2 when r1 < 0.0 && r2 > 0.0 -> TwoRoots (Math.Sqrt(r2), -Math.Sqrt(r2))
        |r1, r2 when r2 < 0.0 && r1 > 0.0 -> TwoRoots (Math.Sqrt(r1), -Math.Sqrt(r1))
        |r1, r2 when r1 = 0.0 && r2 > 0.0 -> ThreeRoots (0.0, Math.Sqrt(r2), -Math.Sqrt(r2))
        |r1, r2 when r2 = 0.0 && r1 > 0.0 -> ThreeRoots (0.0, Math.Sqrt(r1), -Math.Sqrt(r1))
        |r1, r2 -> FourRoots (Math.Sqrt(r1), -Math.Sqrt(r1), Math.Sqrt(r2), -Math.Sqrt(r2))

let PrintRoots(a: double, b: double, c: double): unit =
    printf "Коэффициенты: a=%f, b=%f, c=%f. " a b c
    match CalculateRoots(a, b, c) with
    | NoRoots -> printfn "Нет корней"
    | OneRoot(rt) -> printfn "Один корень: %f" rt
    | TwoRoots(rt1, rt2) -> printfn "Два корня: %f и %f" rt1 rt2
    | ThreeRoots(rt1, rt2, rt3) -> printfn "Три корня: %f, %f и %f" rt1 rt2 rt3
    | FourRoots(rt1, rt2, rt3, rt4) -> printfn "Четыре корня: %f, %f, %f и %f" rt1 rt2 rt3 rt4

let rec readFloat() =
    printfn "Введите коэффициент:"
    match System.Double.TryParse(System.Console.ReadLine()) with
    | false, _ -> 
        printf "Ошибка: введено не число. Повторите ввод коэффициента"
        readFloat()
    | true, x -> x

[<EntryPoint>]
let main argv =
    let a = readFloat()
    let b = readFloat()
    let c = readFloat()

    PrintRoots(a, b, c)

    Console.ReadLine() |> ignore
    0



 