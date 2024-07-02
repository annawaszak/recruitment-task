import React, { useState } from 'react';
import Modal from 'react-modal';

interface ImageModalProps {
  isOpen: boolean;
  onRequestClose: () => void;
  imageUrl: string | null;
  currentIndex: number | null;
  changeImage: (id: number) => void;
}

const ImageModal: React.FC<ImageModalProps> = ({ isOpen, onRequestClose, imageUrl, currentIndex, changeImage }) => {
  const [newId, setNewId] = useState<number | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setNewId(Number(e.target.value));
  };

  const handleSubmit = () => {
    if (newId !== null) {
      changeImage(newId);
    }
  };

  return (
    <Modal isOpen={isOpen} onRequestClose={onRequestClose} contentLabel="Image Modal">
      <h2>Image Details</h2>
      {imageUrl && <img src={imageUrl} alt="Current" />}
      <div>
        <label>Change Image ID: </label>
        <input type="number" onChange={handleChange} />
        <button onClick={handleSubmit}>Submit</button>
      </div>
      <button onClick={onRequestClose}>Close</button>
    </Modal>
  );
};

export default ImageModal;
