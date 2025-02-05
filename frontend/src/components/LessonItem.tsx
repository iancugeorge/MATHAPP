// src/components/LessonItem.tsx
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Lesson } from "../types/Lesson";
import { ExerciseNode } from "../types/ExerciseNode";
interface LessonItemProps {
  lesson: Lesson;
  depth?: number; // to control indentation for nested levels
}

const LessonItem: React.FC<LessonItemProps> = ({ lesson, depth = 0 }) => {
  const navigate = useNavigate();
  const [isOpen, setIsOpen] = useState(false);

  // If there are children lessons or exercises, we want to toggle the open/close state.
  const hasNestedContent = (lesson.children && lesson.children.length > 0) || (lesson.exercises && lesson.exercises.length > 0);

  const handleLessonClick = () => {
    if (hasNestedContent) {
      setIsOpen((prev) => !prev);
    } else if (lesson.code) {
      // If there’s no nested content, navigate directly (this may be a single-lesson page or exercise entry)
      navigate(`/exercise/${lesson.code}`);
    }
  };

  const handleExerciseClick = (exerciseCode: string) => {
    navigate(`/exercise/${exerciseCode}`);
  };

  return (
    <div className="mb-4">
      <div
        onClick={handleLessonClick}
        className={`flex items-center justify-between p-5 bg-white rounded-lg border border-gray-200 
            shadow hover:shadow-lg transform transition-all duration-200 ease-out 
            ${depth > 0 ? "ml-6 border-l-4 border-blue-400" : ""}`}
      >
         <div>
    <h3 className="text-2xl font-semibold text-gray-800">{lesson.name}</h3>
    <p className="text-gray-600 mt-1">{lesson.description}</p>
  </div>
  {hasNestedContent && (
    <button
      onClick={(e) => {
        e.stopPropagation();
        setIsOpen((prev) => !prev);
      }}
      className="text-blue-500 focus:outline-none text-lg"
      aria-label={isOpen ? "Collapse details" : "Expand details"}
    >
      {isOpen ? "–" : "+"}
    </button>
  )}
</div>

      {isOpen && (
        <div className="mt-3 pl-6 border-l-2 border-gray-300 transition-all duration-300 ease-in-out">
          {/* Render exercises if available */}
          {lesson.exercises &&
            lesson.exercises.map((exercise: ExerciseNode) => (
              <div
                key={exercise.id}
                onClick={() => handleExerciseClick(exercise.code)}
                className="p-2 bg-gray-50 rounded-md mt-2 cursor-pointer hover:bg-blue-50 transition duration-200"
              >
                <p className="text-gray-700">{exercise.name}</p>
              </div>
            ))}

          {/* Render child lessons if available */}
          {lesson.children &&
            lesson.children.map((childLesson: Lesson) => (
              <LessonItem key={childLesson.id} lesson={childLesson} depth={depth + 1} />
            ))}
        </div>
      )}
    </div>
  );
};

export default LessonItem;
