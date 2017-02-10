export interface Collection {
    id: number,
    name: string,
    Count: number,
    views_no: number,
    user_possession: number,
    likes: number,
    publicated: string,
    country: {
        id: number,
        name: string,
        name_ascii: string,
        code: string
    },
    reverse_photo: string,
    obverse_photo: string,
    description: string,
    category: {
        id: number,
        name: string,
        type: {
            id: number,
            name: string,
            subtype: {
                id: number,
                name: string,
                set: {
                    id: number,
                    name: string
                }
            }
        }
    },
    numeration: string
}