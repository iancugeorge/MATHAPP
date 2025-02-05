// SampleData.ts
import { Lesson } from "./Lesson";

export const lessons: Lesson[] = [
  {
    id: 1,
    name: "S1 E1 Radicali",
    description: "Expresii cu radicali, distributivitate și simplificare.",
    // This lesson has direct exercises
    exercises: [
      { id: 101, name: "Exercițiu 1", code: "001" },
      { id: 102, name: "Exercițiu 2", code: "001" },
    ],
    children: [
      {
        id: 11,
        name: "Subtopic: Radicali Avansați",
        description: "Extinde conceptele de radicali.",
        exercises: [
          { id: 111, name: "Exercițiu Avansat 1", code: "001" },
        ],
        children: [
            {
              id: 111,
              name: "Final: Cei Mai Radicali Avansați",
              description: "Extinde Cel Mai Mult conceptele de radicali.",
              exercises: [
                { id: 111, name: "Exercițiu Super Avansat 1", code: "001" },
              ],
            },
          ],
      },
    ],
  },
  {
    id: 2,
    name: "S1 E1 Fractii",
    description: "Expresii cu fracții, distributivitate și simplificare.",
    exercises: [
      { id: 201, name: "Exercițiu 1", code: "002A" },
      { id: 202, name: "Exercițiu 2", code: "002B" },
    ],
    children: [
      {
        id: 21,
        name: "Subtopic: Fracții Complexe",
        description: "Rezolvarea exercițiilor complexe.",
        exercises: [
          { id: 211, name: "Exercițiu Complex 1", code: "002C" },
        ],
      },
      {
        id: 22,
        name: "Subtopic: Simplificări",
        description: "Metode de simplificare a fracțiilor.",
        exercises: [
          { id: 221, name: "Exercițiu Simplificare 1", code: "002D" },
        ],
      },
    ],
  },
  // Add additional lessons as needed…
];
