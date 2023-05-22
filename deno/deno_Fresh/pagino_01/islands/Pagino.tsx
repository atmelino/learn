import { useEffect, useRef, useState } from "preact/hooks";


interface PaginoProps {
    showFirst?: boolean;
    showPrevious?: boolean;
    showNext?: boolean;
    showLast?: boolean;
    page?: number;
    count?: number;
    siblingCount: number;
    boundaryCount: number;
    onChange: (page: number, count: number) => void;
}

export default function Pagino(props: PaginoProps) {
    const showFirst = props.showFirst;
    const showPrevious = props.showPrevious;
    const showNext = props.showNext;
    const showLast = props.showLast;
    const siblingCount = props.siblingCount;
    const boundaryCount = props.boundaryCount;
    const onChange = props.onChange;
    const [pages, setPages] = useState([]);


    let page = 1;
    let count = 8;

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

        onChange(page, count);
        // return this;
    }

    function setPage(page: number) {
        if (page <= 0 || page > count) {
            return;
        }

        // this.page = page;

        onChange(page, count);
        // return this;
    }

    function first() {
        setPage(1);
        // return this;
    }

    function last() {
        setPage(count);
        // return this;
    }

    function next() {
        setPage(page + 1);
        // return this;
    }

    function previous() {
        setPage(page - 1);
        // return this;
    }

    function getPages() {
        const startPages = createStartPages(boundaryCount, count);
        const endPages = createEndPages(boundaryCount, count);

        const siblingsStart = createSiblingsStart(
            boundaryCount,
            count,
            page,
            siblingCount,
        );

        const siblingsEnd = createSiblingsEnd(
            boundaryCount,
            count,
            page,
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

        return pages;
    };


    const renderElement = (page: string) => {
        if (page === "start-ellipsis" || page === "end-ellipsis") {
            return <button key={page}>...</button>;
        }

        return (
            <button
                style={{
                    backgroundColor: page === page ? "#0971f1" : ""
                }}
                key={page}
                onClick={() => hanglePaginoNavigation(page)}
            >
                {page}
            </button>
        );
    };

    function hanglePaginoNavigation(page: number) {
        // if (typeof type === "string") {
        //   pagino[type]?.();
        //   return;
        // }

        setPage(page);
    }

	useEffect(() => {
        // onChange: (page, count) => setPages(_.getPages())
        setPages(getPages())

	}, []);




    return (
        <>
            <div>
                <p class="flex-grow-1 font-bold text-xl">
                    <h1>Page: {page}</h1>
                </p>
                <ul>{pages.map(renderElement)}</ul>
            </div>
        </>
    );


}