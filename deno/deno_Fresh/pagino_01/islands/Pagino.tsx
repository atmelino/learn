import { useEffect, useRef, useState } from "preact/hooks";


interface PaginoProps {
    count: number;
    showFirst?: boolean;
    showPrevious?: boolean;
    showNext?: boolean;
    showLast?: boolean;
    page?: number;
    siblingCount: number;
    boundaryCount: number;
    onChange: (page: number, count: number) => void;
}

export default function Pagino(props: PaginoProps) {
    const count = props.count;
    const showFirst = props.showFirst;
    const showPrevious = props.showPrevious;
    const showNext = props.showNext;
    const showLast = props.showLast;
    const siblingCount = props.siblingCount;
    const boundaryCount = props.boundaryCount;
    const onChange = props.onChange;
    const [pages, setPages] = useState([""]);
    const [currentpage, setCurrentPage] = useState(1);

    const { min, max } = Math;

    const createRange = (start: number, end: number): Array<number> => {
        const length: number = end - start + 1;
        return Array.from({ length }, (_, i) => start + i);
    };

    const createStartPages = (
        boundaryCount: number,
        count: number,
    ): Array<number> => createRange(1, min(boundaryCount, count));

    const createEndPages = (boundaryCount: number, count: number): Array<number> =>
        createRange(max(count - boundaryCount + 1, boundaryCount + 1), count);

    const createSiblingsStart = (
        boundaryCount: number,
        count: number,
        page: number,
        siblingCount: number,
    ): number =>
        max(
            min(page - siblingCount, count - boundaryCount - siblingCount * 2 - 1),
            boundaryCount + 2,
        );

    const createSiblingsEnd = (
        boundaryCount: number,
        count: number,
        page: number,
        siblingCount: number,
        endPages: Array<number>,
    ): number =>
        min(
            max(page + siblingCount, boundaryCount + siblingCount * 2 + 2),
            endPages.length > 0 ? endPages[0] - 2 : count - 1,
        );

    function setCount(count: number) {
        // this.count = count;

        onChange(currentpage, count);
        // return this;
    }

    function getPages() {
        const startPages = createStartPages(boundaryCount, count);
        const endPages = createEndPages(boundaryCount, count);

        const siblingsStart = createSiblingsStart(
            boundaryCount,
            count,
            currentpage,
            siblingCount,
        );

        const siblingsEnd = createSiblingsEnd(
            boundaryCount,
            count,
            currentpage,
            siblingCount,
            endPages,
        );

        let pages: any[] = [];

        pages = pages.concat(showFirst ? ["first"] : []);
        pages = pages.concat(showPrevious ? ["previous"] : []);
        pages = pages.concat(startPages);
        pages = pages.concat(
            siblingsStart > boundaryCount + 2
                ? ["start-ellipsis"]
                : boundaryCount + 1 < count - boundaryCount
                    ? [boundaryCount + 1]
                    : [],
        );
        pages = pages.concat(createRange(siblingsStart, siblingsEnd));
        pages = pages.concat(
            siblingsEnd < count - boundaryCount - 1
                ? ["end-ellipsis"]
                : count - boundaryCount > boundaryCount
                    ? [count - boundaryCount]
                    : [],
        );
        pages = pages.concat(endPages);
        pages = pages.concat(showNext ? ["next"] : []);
        pages = pages.concat(showLast ? ["last"] : []);


        console.log(JSON.stringify(pages));
        return pages;
    }


    const renderElement = (page: string) => {
        const inactive = "px-3 py-2 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
        const active = "z-10 px-3 py-2 leading-tight text-blue-600 border border-blue-300 bg-blue-50 hover:bg-blue-100 hover:text-blue-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white"

        if (page === "start-ellipsis" || page === "end-ellipsis") {
            return <button key={page}>...</button>;
        }

        console.log("current page=" + currentpage);

        return (
            <li
                key={page}
                class={parseInt(page) === currentpage
                    ? active
                    : inactive}
                onClick={() => hanglePaginoNavigation(page)}
            >
                {page}
            </li>
        );
    };

    function hanglePaginoNavigation(page: string) {
        console.log("current page=" + currentpage + " new page=" + page);

        if (page === 'first')
            setCurrentPage(1);

        if (page === 'previous')
            if (currentpage > 1)
                setCurrentPage(currentpage - 1);

        if (page === 'next')
            if (currentpage < count)
                setCurrentPage(currentpage + 1);

        if (page === 'last')
            setCurrentPage(count);

        if (!isNaN(parseInt(page)))
            setCurrentPage(parseInt(page));

        // setPage(currentpage);
        setPages(getPages());

        onChange(page, count);

    }

    useEffect(() => {
        // onChange: (page, count) => setPages(_.getPages())
        setPages(getPages())

    }, []);




    return (
        <>
            <div>
                <p class="flex-grow-1 font-bold text-xl">
                    <h1>Page: {currentpage}</h1>
                </p>
                <nav aria-label="Page navigation example">
                    <ul class="inline-flex items-center -space-x-px">
                        {pages.map(renderElement)}
                    </ul>
                </nav>
            </div>
        </>
    );


}